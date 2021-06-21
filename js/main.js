const input = require('prompt-sync')();
var initial = 20;

console.log("╔═════════════════════╗ \n\n THOUSAND MINUS SEVEN \n\n╚═════════════════════╝");

while (true)
{
    try
    {
        console.log("");
        var ask = parseInt(input(`What's ${initial} - 7: `));
    }

    catch (err)
    {
        console.log("\nYou are a fool, you can't read -takes out your eyeballs-");
        break;
    }
    
    initial -= 7;

    if (ask === initial)
    {
        if (initial < 10)
        {
            console.log("\nCongratulations on completing this torture, now you can go home.. \nYou: Wow really?!\nThanks a lo- -stabs you with his kagune-....");
            break;
        }
        
        else
        {
            continue;
        }
    }

    else
    {
        console.log("\nWrong answer. -inserts earthworms into your ears-");
        break;
    }
}
