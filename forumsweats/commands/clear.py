from forumsweats import confirmgui


name = 'clear'
aliases = ('purge',)
args = '<amount>'
channels = None
roles = ('helper')


async def run(message, amount: int):
	'Purge recent messages'
	if amount > 100:
		verify_message = await message.channel.send(f'Are you sure you want to purge {amount} recent messages?')
		confirmed = await confirmgui.make_confirmation_gui(message.client, verify_message, message.author)
		if not confirmed:
			return
		# add 1 to include this new message
		amount += 1

	await message.channel.purge(limit=amount, check=lambda m: m.id != message.id)