const { description } = require("./avatar");

module.exports = 
{
    name: 'meme',
    description: "this is a meme command!",
    execute(message, args)
    {    
        message.channel.send('Ainda não funciono!!');
    }
}