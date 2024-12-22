# Tom_and_Jerry
# changed Tom_and_Jerry

<!-- [MermaidChart: 6c1f677d-3cdd-465d-ad93-187b5b8323ef] -->
flowchart TD
    Start["Start Game: Jerry's Quest for the Cheese" ] --> DisplayInfo["Navigate the house to get to the Fridge and get cheese. Beware of Tom and mouse traps but the Dog will help you."]
    DisplayInfo --> JerryTurn["Jerry's Turn" ]
    JerryTurn --> DisplayDoors["Display random doors"]
    DisplayDoors --> ChooseDoor["Jerry Chooses a Door"]
    ChooseDoor --> CheckOutcome["The corridor leads to&nbsp; [random room]."]
    CheckOutcome --> Checkoutcome["You can hear Tom purring"]
    Checkoutcome -- Tom --> Tom["Tom is behind the door! Jerry gets caught."]
    Tom --> EndGame["Game Over!"]
    Checkoutcome -- Mouse Trap --> Trapoutcome["You hear snapping"] & Checkoutcome
    Trapoutcome --> Trap["It's a mouse trap! Jerry gets caught."]
    Trap --> EndGame
    Checkoutcome -- Dog --> Dog["It's the dog! Jerry gets a shortcut to the fridge."]
    Dog --> Dogshortcut["One door leads to Fridge"] & ContinueGame["The room is safe. Jerry continues."]
    Dogshortcut -- Cheese --> Cheese["Jerry finds cheese"]
    Cheese --> WinGame["Jerry Wins"]
    WinGame --> EndGame
    ContinueGame --> JerryTurn & Trapoutcome & CheckOutcome
