var dinos = [
    {
        name: "Littlefoot", 
        type: "Brontosaurus", 
        age: 145500000, 
        isAlive: false
    },
    {
        name: "Steve", 
        type: "Operations Director", 
        age: 44, 
        isAlive: true
    },
    {
        name: "Barry", 
        type: "Release Dinosaur", 
        age: 44, 
        isAlive: false
    },
    {
        name: "Non-Trademark-Violating-Zilla", 
        type: "Godlike", 
        age: 64, 
        isAlive: false
    }
];

const app = Vue.createApp({
    data() {
      return {
        dinos: dinos,
        search: '',
        count: 0,
        error: false,
      }
    },
    methods: {
        sortByAge() {
            this.count++
            if (this.count % 2 === 0) {  
                this.dinos.sort((a, b) => a.age - b.age) // Sort the list in ascending order
            } else {
                this.dinos.sort((a, b) => b.age - a.age) // Sort the list in descending order
            }
        },
    },
    watch: {
        search(value) {
            if (value === '') {  // If the search bar is empty, reset the list
                this.dinos = dinos  // Reset the list
            } else {
                this.error = false  // If the search bar is not empty, reset the error message
                this.dinos = dinos.filter(dino => {
                    return dino.name.toLowerCase().includes(this.search.toLowerCase())  // Filter the list based on the search input
                })

                if (this.dinos.length === 0) {
                    this.error = true // If no results are found, display an error message
                    return this.dinos = dinos  // Ensure that the list is reset if the search returns no results
                }
            }
        }
    }
  })

 app.mount('#app')