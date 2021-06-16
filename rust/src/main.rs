use std::io;

fn main()
{

    println!("╔═════════════════════╗ \n\n TORTURE FROM JSON \n\n╚═════════════════════╝\n");

    let mut initial = 1000;

    loop
    {

        println!("What's {} - 7", initial);

        let mut answer = String::new();

        io::stdin()
            .read_line(&mut answer)
            .expect("\nWrong answer. -inserts earthworms into your ears-");

        initial -= 7;

        let answer: u32 = match answer.trim().parse()
        {
            Ok(num) => num,
            Err(_) => {println!("\nYou are a fool, you can't read -takes out your eyeballs-");return;},
        };

        if answer == initial {
            continue;
        }

        else if answer < 10 && initial < 10
        {
            println!("\nCongratulations on completing this torture, now you can go home.. \nYou: Wow really?! Thanks a lo- -stabs you with his kagune-....");
            break;
        }
        
        else {
            print!("\nWrong answer. -inserts earthworms into your ears-");
            break;
        }
    }
}
