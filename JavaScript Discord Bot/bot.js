const Discord = require('discord.js');
const client = new Discord.Client();

const prefix = '-';//prefixo do comando
const fs = require('fs');
 
client.commands = new Discord.Collection();
 
const commandFiles = fs.readdirSync('./commands/').filter(file => file.endsWith('.js'));
for(const file of commandFiles)
{  
     const command = require(`./commands/${file}`);
     client.commands.set(command.name, command);
}
 
client.once('ready', () => { console.log('Bots está a funcionar Caralho!!!!');});//quando o bot liga
 
client.on('message', message =>{
    if(!message.content.startsWith(prefix) || message.author.bot) return;
 
    const args = message.content.slice(prefix.length).split(/ +/);
    const command = args.shift().toLowerCase();//coloca todos os comandos para miniscula para não haver casos que n funcione
 
    if(command === 'vine')
    {
        client.commands.get('vine').execute(message, args);
    }
    else if (command === 'clear')
    {
            client.commands.get('clear').execute(message, args);    
    } 
    else if (command ===  'avatar')
    {
        	  client.commands.get('avatar').execute(message, args);
    }else if (command ===  'help')
    {
        	  client.commands.get('help').run(client, message, args);
    }
});
 
client.login('NzM5MzA5NTM3MTEwMjYxODIx.XyYlqQ._e7oq04r0VbIJ2tF33ZsMR7llS4');