from colorama import Back, Fore

imgs = {
    "a": {
      "arch":
        {
            "logo": 
                [
                    Back.CYAN + Fore.BLACK + "          " + Fore.RESET + Back.RESET,
                    Back.CYAN + Fore.BLACK + "    /\    " + Fore.RESET + Back.RESET,
                    Back.CYAN + Fore.BLACK + "   /  \   " + Fore.RESET + Back.RESET,
                    Back.CYAN + Fore.BLACK + "  /_/\_\  " + Fore.RESET + Back.RESET,
                    Back.CYAN + Fore.BLACK + "          " + Fore.RESET + Back.RESET,
                ],

            "text": Fore.CYAN
        },

        "alpine":
            {
                "logo":
                    [
                        Back.BLUE + Fore.BLACK + "          " + Fore.RESET + Back.RESET,
                        Back.BLUE + Fore.BLACK + "   /\     " + Fore.RESET + Back.RESET,
                        Back.BLUE + Fore.BLACK + "  //\\\/\  " + Fore.RESET + Back.RESET,
                        Back.BLUE + Fore.BLACK + " //  \\\\\\\ " + Fore.RESET + Back.RESET,
                        Back.BLUE + Fore.BLACK + "          " + Fore.RESET + Back.RESET,
                    ],
                "text": Fore.BLUE
            },

        "arco":
            {
                "logo":
                    [
                        Back.BLUE + Fore.BLACK + "          " + Fore.RESET + Back.RESET,
                        Back.BLUE + Fore.BLACK + "    /\    " + Fore.RESET + Back.RESET,
                        Back.BLUE + Fore.BLACK + "   //\\\   " + Fore.RESET + Back.RESET,
                        Back.BLUE + Fore.BLACK + "  // -=\  " + Fore.RESET + Back.RESET,
                        Back.BLUE + Fore.BLACK + "          " + Fore.RESET + Back.RESET,
                    ],
                "text": Fore.BLUE
            }
    },

    "b": 
        {
            "bedrock":
                {
                    "logo":
                        [
                            Back.BLACK + Fore.WHITE + " __       " + Fore.RESET + Back.RESET,
                            Back.BLACK + Fore.WHITE + " \ \___   " + Fore.RESET + Back.RESET,
                            Back.BLACK + Fore.WHITE + "  \  _ \  " + Fore.RESET + Back.RESET,
                            Back.BLACK + Fore.WHITE + "   \___/  " + Fore.RESET + Back.RESET,
                            Back.BLACK + Fore.WHITE + "          " + Fore.RESET + Back.RESET,
                        ],
                    "text": Fore.WHITE
                }
            
        },
    
    "d":
        {
            "debian":
                {
                    "logo":
                        [
                            Back.RED + Fore.BLACK + "     __   " + Fore.RESET + Back.RESET,
                            Back.RED + Fore.BLACK + "  '/  .\\' " + Fore.RESET + Back.RESET,
                            Back.RED + Fore.BLACK + "  |  (_'  " + Fore.RESET + Back.RESET,
                            Back.RED + Fore.BLACK + "   \      " + Fore.RESET + Back.RESET,
                            Back.RED + Fore.BLACK + "          " + Fore.RESET + Back.RESET,
                        ],
                    "text": Fore.RED
                }
        },

    "e":
        {
            "endeavouros":
                {
                    "logo":
                        [
                            Back.LIGHTMAGENTA_EX + Fore.BLACK + "     __   " + Fore.RESET + Back.RESET,
                            Back.LIGHTMAGENTA_EX + Fore.BLACK + "    /  \  " + Fore.RESET + Back.RESET,
                            Back.LIGHTMAGENTA_EX + Fore.BLACK + "  /     | " + Fore.RESET + Back.RESET,
                            Back.LIGHTMAGENTA_EX + Fore.BLACK + " '_____/  " + Fore.RESET + Back.RESET,
                            Back.LIGHTMAGENTA_EX + Fore.BLACK + "          " + Fore.RESET + Back.RESET,
                        ],
                    "text": Fore.LIGHTMAGENTA_EX
                }
        },
    
    "f":
        {
            "fedora":
                {
                    "logo":
                        [
                            Back.BLACK + Fore.BLUE + "   ____   ",
                            Back.BLACK + Fore.BLUE + "  /  " + Fore.WHITE + "_" + Fore.BLUE + " \  " + Fore.RESET + Back.RESET,
                            Back.BLACK + Fore.BLUE + " | " + Fore.WHITE + "C/-" + Fore.BLUE + "  | " + Fore.RESET + Back.RESET,
                            Back.BLACK + Fore.BLUE + " |_____/  " + Fore.RESET + Back.RESET,
                            Back.BLACK + Fore.BLUE + "          " + Fore.RESET + Back.RESET,
                        ],
                    "text": Fore.BLUE
                }
        },
    "g":
        {
            "gentoo":
                {
                    "logo":
                        [
                            Back.WHITE + Fore.BLACK + "   ___    " + Fore.RESET + Back.RESET,
                            Back.WHITE + Fore.BLACK + "  [  _ \  " + Fore.RESET + Back.RESET,
                            Back.WHITE + Fore.BLACK + "   >   /  " + Fore.RESET + Back.RESET,
                            Back.WHITE + Fore.BLACK + "  (__ /   " + Fore.RESET + Back.RESET,
                            Back.WHITE + Fore.BLACK + "          " + Fore.RESET + Back.RESET,
                        ],
                    "text": Fore.WHITE
                }
        },
    "m":
        {
            "manjaro":
                {
                    "logo":
                        [
                            Back.GREEN + Fore.BLACK + " ,___,,_, " + Fore.RESET + Back.RESET,
                            Back.GREEN + Fore.BLACK + " | ,_|| | " + Fore.RESET + Back.RESET,
                            Back.GREEN + Fore.BLACK + " | |  | | " + Fore.RESET + Back.RESET,
                            Back.GREEN + Fore.BLACK + " |_|__|_| " + Fore.RESET + Back.RESET,
                            Back.GREEN + Fore.BLACK + "          " + Fore.RESET + Back.RESET,
                        ],
                    "text": Fore.GREEN
                },
        },
    "n":
        {
            "nixos":
                {
                    "logo":
                        [
                            Back.BLACK + Fore.BLACK + "          " + Fore.RESET + Back.RESET,
                            Back.BLACK + Fore.BLUE + "   ==" + Fore.CYAN + "\\\\   " + Fore.RESET + Back.RESET,
                            Back.BLACK + Fore.CYAN + "  // " + Fore.BLUE + " //  " + Fore.RESET + Back.RESET,
                            Back.BLACK + Fore.BLUE + "   \\" + "\\" + Fore.CYAN + "==   " + Fore.RESET + Back.RESET,
                            Back.BLACK + Fore.BLACK + "          " + Fore.RESET + Back.RESET,
                        ],
                    "text": Fore.CYAN
                },
        },
    "o":
        {
            "opensuse-leap":
                {
                    "logo":
                        [
                            Back.GREEN + Fore.BLACK + "    ,___  " + Fore.RESET + Back.RESET,
                            Back.GREEN + Fore.BLACK + "   _| ()\ " + Fore.RESET + Back.RESET,
                            Back.GREEN + Fore.BLACK + " /    --' " + Fore.RESET + Back.RESET,
                            Back.GREEN + Fore.BLACK + " \ __^/   " + Fore.RESET + Back.RESET,
                            Back.GREEN + Fore.BLACK + "          " + Fore.RESET + Back.RESET,
                        ],
                    "text": Fore.GREEN
                },
            "opensuse-tumbleweed":
                {
                    "logo":
                        [
                            Back.BLUE + Fore.BLACK + "  _    _  " + Fore.RESET + Back.RESET,
                            Back.BLUE + Fore.BLACK + " / \  / \ " + Fore.RESET + Back.RESET,
                            Back.BLUE + Fore.BLACK + " |  )(  | " + Fore.RESET + Back.RESET,
                            Back.BLUE + Fore.BLACK + " \_/  \_/ " + Fore.RESET + Back.RESET,
                            Back.BLUE + Fore.BLACK + "          " + Fore.RESET + Back.RESET,
                        ],
                    "text": Fore.BLUE
                }
        },
    "s":
        {
            "slackware":
                {
                    "logo":
                        [
                            Back.BLUE + Fore.BLACK + "          " + Fore.RESET + Back.RESET,
                            Back.BLUE + Fore.BLACK + "   ,-=|   " + Fore.RESET + Back.RESET,
                            Back.BLUE + Fore.BLACK + "   '==,   " + Fore.RESET + Back.RESET,
                            Back.BLUE + Fore.BLACK + "   |=-'   " + Fore.RESET + Back.RESET,
                            Back.BLUE + Fore.BLACK + "          " + Fore.RESET + Back.RESET,
                        ],
                    "text": Fore.BLUE
                }
        },
    "u":
        {
            "ubuntu":
                {
                    "logo":
                        [
                            Back.YELLOW + Fore.BLACK + "    __    " + Fore.RESET + Back.RESET,
                            Back.YELLOW + Fore.BLACK + " () -- () " + Fore.RESET + Back.RESET,
                            Back.YELLOW + Fore.BLACK + " | |  | | " + Fore.RESET + Back.RESET,
                            Back.YELLOW + Fore.BLACK + "  \ -- /  " + Fore.RESET + Back.RESET,
                            Back.YELLOW + Fore.BLACK + "    ''    " + Fore.RESET + Back.RESET,
                        ],
                    "text": Fore.YELLOW
                }
        },
    
    "v":
        {
            "void":
                {
                    "logo":
                        [
                            Back.BLACK + Fore.WHITE + "    __    ",
                            Back.BLACK + Fore.GREEN + "  ," + Fore.WHITE + "\   \  ",
                            Back.BLACK + Fore.GREEN + " |'" + "\\" + Fore.WHITE + "()\,| ",
                            Back.BLACK + Fore.GREEN + "  \ __\\'  ",
                            Back.BLACK + Fore.GREEN + "          ",
                        ],
                    "text": Fore.GREEN
                }
        }
}

if __name__ == "__main__":
    for l in logos["v"]["void"]["logo"]:
        print(l + logos["v"]["void"]["text"] + f" placeholder{Fore.RESET} │ another_placeholder")