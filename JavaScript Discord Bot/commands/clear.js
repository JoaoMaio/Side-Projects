module.exports = 
{
    name: 'clear',
    description: "this is a clear command!",
    execute(message, args)
    {    
                message.delete();
                const fetched = 99
                message.channel.bulkDelete(fetched);
                message.channel.send('Mensagens Eliminadas!!');
    }
}