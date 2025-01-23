module.exports = 
{
    name: 'vine',
    description: "this is a vine command!",
    execute(message, args)
    {
        message.channel.send('Random Vine For'+ ' ' + `${message.author},` + ' ' + 'Pussy');
        
        var videosvine = 
            	[
            	"https://www.youtube.com/watch?v=6mOQeCnJWRM", 
            	"https://www.youtube.com/watch?v=DYzT-Pk6Ogw", 
            	"https://www.youtube.com/watch?v=fdAqre8X3hI",
            	"https://www.youtube.com/watch?v=c3m4Q07TkMk",
                "https://www.youtube.com/watch?v=eEa3vDXatXg",
                "https://www.youtube.com/watch?v=21jLmc_Il3o&list=PLqjEF1rwSoHmB5ktOSZgB4I_Z40UmrFNB",
                "https://www.youtube.com/watch?v=dNavpxx_PPk&list=PLqjEF1rwSoHmB5ktOSZgB4I_Z40UmrFNB&index=2",
                "https://www.youtube.com/watch?v=Jk6jVl1fAn0&list=PLqjEF1rwSoHmB5ktOSZgB4I_Z40UmrFNB&index=3",
                "https://www.youtube.com/watch?v=KeFeGms9Jls&list=PLqjEF1rwSoHmB5ktOSZgB4I_Z40UmrFNB&index=4",
                "https://www.youtube.com/watch?v=_T1wBFWbf-g&list=PLqjEF1rwSoHmB5ktOSZgB4I_Z40UmrFNB&index=5",
                "https://www.youtube.com/watch?v=S9-p_w6V6IA&list=PLqjEF1rwSoHmB5ktOSZgB4I_Z40UmrFNB&index=6",
                "https://www.youtube.com/watch?v=nEpt_EIal-c&list=PLqjEF1rwSoHmB5ktOSZgB4I_Z40UmrFNB&index=7",
                "https://www.youtube.com/watch?v=aUfxqxMnHjA&list=PLqjEF1rwSoHmB5ktOSZgB4I_Z40UmrFNB&index=8",
                "https://www.youtube.com/watch?v=feMwFuihX2o&list=PLqjEF1rwSoHmB5ktOSZgB4I_Z40UmrFNB&index=9",
                "https://www.youtube.com/watch?v=37hM3x5GODk&list=PLqjEF1rwSoHmB5ktOSZgB4I_Z40UmrFNB&index=10",
                "https://www.youtube.com/watch?v=s5BSAIUSUc4&list=PLqjEF1rwSoHmB5ktOSZgB4I_Z40UmrFNB&index=11",
                "https://www.youtube.com/watch?v=8y7EBA5GMJk&list=PLqjEF1rwSoHmB5ktOSZgB4I_Z40UmrFNB&index=12",
                "https://www.youtube.com/watch?v=hHH5Un2y9ug&list=PLqjEF1rwSoHmB5ktOSZgB4I_Z40UmrFNB&index=13",
                "https://www.youtube.com/watch?v=zDgc3LTiF9U&list=PLqjEF1rwSoHmB5ktOSZgB4I_Z40UmrFNB&index=14",
                "https://www.youtube.com/watch?v=ZzWqfJFxC0w&list=PLqjEF1rwSoHmB5ktOSZgB4I_Z40UmrFNB&index=15",
                "https://www.youtube.com/watch?v=mf1ChkziFIQ&list=PLqjEF1rwSoHmB5ktOSZgB4I_Z40UmrFNB&index=18",
                "https://www.youtube.com/watch?v=anWF8v1FesU&list=PLqjEF1rwSoHmB5ktOSZgB4I_Z40UmrFNB&index=19",
                "https://www.youtube.com/watch?v=S_Zl21ybecU&list=PLqjEF1rwSoHmB5ktOSZgB4I_Z40UmrFNB&index=20",
                "https://www.youtube.com/watch?v=94LHw8fa_GE&list=PLqjEF1rwSoHmB5ktOSZgB4I_Z40UmrFNB&index=21",
                "https://www.youtube.com/watch?v=ei0ds1Dj6_c&list=PLqjEF1rwSoHmB5ktOSZgB4I_Z40UmrFNB&index=22",
                "https://www.youtube.com/watch?v=Zx4zAZTmQ40&list=PLqjEF1rwSoHmB5ktOSZgB4I_Z40UmrFNB&index=23",
                "https://www.youtube.com/watch?v=g_KlxoVHUmM&list=PLqjEF1rwSoHmB5ktOSZgB4I_Z40UmrFNB&index=24",
                "https://www.youtube.com/watch?v=g6cIYDvFS-U&list=PLqjEF1rwSoHmB5ktOSZgB4I_Z40UmrFNB&index=25",
                "https://www.youtube.com/watch?v=gnavcUHC6zc&list=PLqjEF1rwSoHmB5ktOSZgB4I_Z40UmrFNB&index=26",
                "https://www.youtube.com/watch?v=kZSfPPJ4Fk8&list=PLqjEF1rwSoHmB5ktOSZgB4I_Z40UmrFNB&index=27",
                "https://www.youtube.com/watch?v=z5gWGBIP9lI&list=PLqjEF1rwSoHmB5ktOSZgB4I_Z40UmrFNB&index=28",
                "https://www.youtube.com/watch?v=4Hz3RpiljFk&list=PLqjEF1rwSoHmB5ktOSZgB4I_Z40UmrFNB&index=29",
                "https://www.youtube.com/watch?v=jfviUbgGimw&list=PLqjEF1rwSoHmB5ktOSZgB4I_Z40UmrFNB&index=30",
                "https://www.youtube.com/watch?v=y-P0m0M_8pc&list=PLqjEF1rwSoHmB5ktOSZgB4I_Z40UmrFNB&index=33",
                "https://www.youtube.com/watch?v=Eywp61pXUm4&list=PLqjEF1rwSoHmB5ktOSZgB4I_Z40UmrFNB&index=34",
                "https://www.youtube.com/watch?v=EwAajOtfNT8&list=PLqjEF1rwSoHmB5ktOSZgB4I_Z40UmrFNB&index=35",
                "https://www.youtube.com/watch?v=GAxD39rGUeE&list=PLqjEF1rwSoHmB5ktOSZgB4I_Z40UmrFNB&index=36",
                "https://www.youtube.com/watch?v=T-E7-tHWQMo&list=PLqjEF1rwSoHmB5ktOSZgB4I_Z40UmrFNB&index=37",
                "https://www.youtube.com/watch?v=uu_h8l4cYnU&list=PLqjEF1rwSoHmB5ktOSZgB4I_Z40UmrFNB&index=38",
                "https://www.youtube.com/watch?v=YtSPQIK15uc&list=PLqjEF1rwSoHmB5ktOSZgB4I_Z40UmrFNB&index=39",
                "https://www.youtube.com/watch?v=7ipu5QTlpLY&list=PLqjEF1rwSoHmB5ktOSZgB4I_Z40UmrFNB&index=40",
                "https://www.youtube.com/watch?v=GouWVUFQoJg&list=PLqjEF1rwSoHmB5ktOSZgB4I_Z40UmrFNB&index=41",
                "https://www.youtube.com/watch?v=du-TY1GUFGk&list=PLqjEF1rwSoHmB5ktOSZgB4I_Z40UmrFNB&index=42",
                "https://www.youtube.com/watch?v=ndl__n35IjY&list=PLqjEF1rwSoHmB5ktOSZgB4I_Z40UmrFNB&index=43",
                "https://www.youtube.com/watch?v=Obgnr9pc820&list=PLqjEF1rwSoHmB5ktOSZgB4I_Z40UmrFNB&index=44",
                "https://www.youtube.com/watch?v=Jk7rbxu6bu8&list=PLqjEF1rwSoHmB5ktOSZgB4I_Z40UmrFNB&index=45",
                "https://www.youtube.com/watch?v=eJtZKXqDi64&list=PLqjEF1rwSoHmB5ktOSZgB4I_Z40UmrFNB&index=46",
                "https://www.youtube.com/watch?v=9lc0SNdx7hc&list=PLqjEF1rwSoHmB5ktOSZgB4I_Z40UmrFNB&index=47",
                "https://www.youtube.com/watch?v=au-04H2bGkY&list=PLqjEF1rwSoHmB5ktOSZgB4I_Z40UmrFNB&index=50",
                "https://www.youtube.com/watch?v=R8nanG0LdjU&list=PLqjEF1rwSoHmB5ktOSZgB4I_Z40UmrFNB&index=51",
                "https://www.youtube.com/watch?v=SyPiD_KqdIE&list=PLqjEF1rwSoHmB5ktOSZgB4I_Z40UmrFNB&index=52",
                "https://www.youtube.com/watch?v=pZUWzDC1kMM&list=PLqjEF1rwSoHmB5ktOSZgB4I_Z40UmrFNB&index=59&t=0s"                
                ];
        var video = Math.floor(Math.random() * 51)
        message.channel.send(videosvine[video]);   
    }
}