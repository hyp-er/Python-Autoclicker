# Configuration:

Follow the directions below for information on how to configure the autoclicker settings.

###### Clicking Speed
To change the **clicking speed** of the auto clicker, go over to "**time.sleep(0.1)**" and switch the "0.1" to whatever time you want. if you set the variable to 1, that would be equal to 1 second. please do not delete this, as it prevents lag and possible crashes.

###### Click Type
If you want the auto clicker to change to a **different click** (I.E. left click to right click) then go over to where it shows "**mouse.press(Button.left)**" and "**mouse.release(Button.left)**", and change the "left" to "right". Doing this will make you spam the right-click, and not left click. If you want to switch back to the normal auto clicker, **undo** the changes you made.

###### Amount of Clicks
In order to change the **amount of clicks** that happen before the loop stops, go to "for x in range(50):" and change the "(50)" to however many times you want the autoclicker to click. If you want it to be **infinite**, delete the entire line of code and write "**while True:**" (*capitals are necessary*)
