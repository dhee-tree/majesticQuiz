# Majestic Quiz (Test B - Vue and reactive frameworks)

## By: Ighomena Odebala

### Task
Create a webpage using the Vue framework to display this data in a table. Then attempt to add the following:
- A button to sort the dinosaurs by age
- An input box to filter the table by name (for example, typing in “little” would filter out every entry except “Littlefoot”).

#### Approach
- I used the Vue framework to create the webpage.
- I used external stylesheet and script tags to link the CSS and JS files to the HTML file.
- I used the `v-for` directive to loop through the data and display it in a table.
- I used the `v-model` directive to bind the input value to a data property.
- I used the `v-show` directive to show and hide the message when the name entered is not in the table.
- I used the `methods` object to create a method that sorts the dinosaurs by age.
- I used the `watch` object to create a watcher that filters the table by name.

#### Resources
- [Vue Methods - W3Shools](https://www.w3schools.com/vue/vue_methods.php)
- [Vue Watcher - W3Shools](https://www.w3schools.com/vue/vue_watchers.php)
- [Vue v-show - W3Shools](https://www.w3schools.com/vue/vue_v-show.php)

## Technologies used
- [HTML](https://www.w3.org/html/)
- [CSS](https://www.w3.org/css/)
- [JavaScript](https://www.javascript.com/)
- [Vue](https://vuejs.org/)
- [Bootstrap](https://getbootstrap.com/)
- [Cloudflare](https://www.cloudflare.com/)
- [GitHub Pages](https://pages.github.com/)

## Installation
- No installation required

## Usage
1. Open the `index.html` file in a web browser.
2. The webpage would be displayed.
3. Click the `Sort by Age` button to sort the dinosaurs by age in ascending order.
4. Clicking the button again would reverse the sorting.
5. Enter the name of the dinosaur you want to filter in the input box and press enter.
6. The table would be filtered by the name entered.
7. If the name entered is not in the table, a message would be displayed to inform you that the name is not in the table.

## Accessing the Webpage
The webpage can be accessed [here](https://vue.ighomena.me)