from datetime import datetime

from discord import ButtonStyle, Colour, Embed, Intents, Interaction, ui
from discord.ext.commands import Bot

from vshieldpy import Client, api_defs
from vshieldpy.exceptions.base_exception import VShieldpyException
from vshieldpy.exceptions.id_exceptions import InvalidServerID

bot = Bot(intents=Intents.none(), command_prefix="!")
vs_client = Client("VSHIELD_API_TOKEN")

# While discord user id's are numbers it is stored as a string to avoid
# accidental mutability as a safety guard. Still doesnt protect from assignment
# so beware.
discord_user_id = "YOUR_USER_ID"


class ActionButton(ui.Button):
    def __init__(self, action, callback, server_id: int):
        super().__init__(label=action.name, style=ButtonStyle.green)
        self.action = action
        self._callback = callback
        self.server_id = server_id

    async def callback(self, interaction: Interaction):
        await interaction.response.defer()
        await self._callback(self.server_id, self.action)
        embed = Embed(
            title="Executing Task",
            description=f"Started {self.action.name} task for server #{self.server_id}.",
            colour=VS_COLOR,
        )
        await interaction.followup.send(embed=embed, ephemeral=True)


# This checks if the current user is authenticated to issue commands.
# We could also just decorate each and every command but this approach is simpler
# since we only want a single user to be able to issue commands. Keep in mind this
# affects all commands from the discord bot.
# Also allows the bot itself to invoke commands.
async def check_user_id(interaction: Interaction):
    if str(interaction.user.id) == discord_user_id or interaction.user.id == str(
        # This is fine since it is only called where a user SHOULD be present.
        bot.user.id  # type: ignore
    ):
        return True

    embed = Embed(
        title="Bad User",
        description="Only the authorized user can issue commands.",
        colour=Colour.red(),
    )
    await interaction.response.send_message(embed=embed, ephemeral=True)
    return False


bot.tree.interaction_check = check_user_id
VS_COLOR = Colour.from_rgb(12, 127, 242)


@bot.tree.command(
    name="start_server_task",
    description=(
        "Executes a task on a server."
        "If Reinstall is selected you must provide an os argument."
    ),
)
async def start_server_task(
    interaction: Interaction,
    server_id: int,
    action: api_defs.ServerActions,
    os: api_defs.OperatingSystems | None = None,
):
    await interaction.response.defer(ephemeral=True)
    try:
        task_id = await vs_client.create_server_task(server_id, action, os)
    except InvalidServerID:
        return
    embed = Embed(
        title="Executing Task",
        description=f"Task for server with ID {server_id} has been started.",
    )

    embed.add_field(name="Task action", value=action.name)
    embed.add_field(name="Task ID", value=str(task_id))
    embed.colour = VS_COLOR

    await interaction.followup.send(embed=embed, ephemeral=True)


@bot.tree.command(
    name="connect_to_server",
    description=("Get the URI to connect to the server via the web browser."),
)
async def connect_to_server(interaction: Interaction, server_id: int):
    await interaction.response.defer(ephemeral=True)
    server_uri = await vs_client.fetch_server_console(server_id)
    embed = Embed(
        title="NoVNC connection requested",
        description=f"Click [here]({server_uri}) to connect to the server via the browser.",
        colour=VS_COLOR,
    )
    await interaction.followup.send(embed=embed, ephemeral=True)


@bot.tree.command(
    name="get_server",
    description=(
        "Returns a specific server."
        " Allows easy control over common use actions on a server."
    ),
)
async def get_server(interaction: Interaction, hostname: str):
    await interaction.response.defer(ephemeral=True)
    servers = await vs_client.fetch_servers()
    server = servers.get_server_from_hostname(hostname)[0]
    embed = Embed(title=f"Server {hostname} | {server.identifier}", colour=VS_COLOR)
    embed.add_field(name="Hostname", value=server.hostname)
    embed.add_field(name="IP", value=server.ip)
    embed.add_field(name="Status", value="Running" if server.status else "Stopped")
    embed.add_field(name="Operating System", value=server.os.name)
    embed.add_field(name="Plan", value=server.plan.name)
    embed.add_field(name="Node", value=server.node)
    embed.add_field(name="Auto-renew", value=f"{server.autorenew.name}d")
    embed.add_field(
        name="Expiration",
        value=f"<t:{int(datetime.timestamp(server.expiration))}>",
    )
    view = ui.View()
    view.add_item(
        ActionButton(
            api_defs.ServerActions.Start,
            vs_client.create_server_task,
            server.identifier,
        )
    )
    view.add_item(
        ActionButton(
            api_defs.ServerActions.Stop, vs_client.create_server_task, server.identifier
        )
    )
    view.add_item(
        ActionButton(
            api_defs.ServerActions.Restart,
            vs_client.create_server_task,
            server.identifier,
        )
    )
    view.add_item(
        ActionButton(
            api_defs.ServerActions.FixNetwork,
            vs_client.create_server_task,
            server.identifier,
        )
    )
    await interaction.followup.send(embed=embed, view=view, ephemeral=True)


@bot.tree.error
async def handle_vs_exceptions(interaction: Interaction, error):
    if isinstance(error.original, VShieldpyException):
        original = error.original
        if isinstance(original, InvalidServerID):
            embed = Embed(
                title="Invalid Server ID provided.",
                description="Please check if the server exists.",
                colour=Colour.red(),
                # TODO add button to list servers in embed.
            )
        else:  # Handles all other api exceptions.
            embed = Embed(
                title="Unkown Error.",
                description="Unkown error from vShield API was found.",
                colour=Colour.red(),
            )
        await interaction.followup.send(embed=embed, ephemeral=True)
        return
    else:  # Possibly handle exceptions from other libraries before this.
        embed = Embed(
            title="Unkown Error.", description="Unkown error", colour=Colour.red()
        )
    await interaction.response.send_message(embed=embed, ephemeral=True)


@bot.event
async def on_ready():
    await bot.tree.sync()


bot.run("YOUR_TOKEN")
