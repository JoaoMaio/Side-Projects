module.exports = 
{
        name: 'help',
        description: 'Mostra todos os comandos disponíveis do bot.',

    run: (client, message, args) => 
    {
      const mensagem = 
      {
        color: 0xE59442,
        title: 'Lista dos comandos',
        description: '[Clique aqui para ir para o site(https://pt.wikihow.com/P%C3%A1gina-principal)',
        timestamp: new Date(),
        footer: {text: 'Autismo Puro'},
        fields: []
      }

      mensagem.fields.push({
          name: 'Ajuda',
          value: ` Mostra todos os comandos disponíveis do bot. `,
        })
        mensagem.fields.push({
            name: 'Meme',
            value: `Manda um random meme`,
          })
          mensagem.fields.push({
            name: 'Vine',
            value: `Manda um random vine.`,
          })
          mensagem.fields.push({
            name: 'Clear',
            value: `Limpa 99 Mensagens.`,
          })
          mensagem.fields.push({
            name: 'Avatar',
            value: `Manda o teu avatar em forma de imagem.`,
          })
  
      message.channel.send({ embed: mensagem })
        .then(() => message.react('⚡'))
    },
  }