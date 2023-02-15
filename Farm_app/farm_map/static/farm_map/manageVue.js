const app = Vue.createApp({
    // get around conflict with Jinja/Django/JavaScript delimiters conflicting
        delimiters: ['--','--'],
    data(){
        return{
            test : 'test success',
            zones : [],
            pokeSearch: null,
            csrfToken : document.getElementsByName('csrfmiddlewaretoken'),
            return: []
            
            
        }
    },
    methods: {
        searchPokemon: function(){
            fetch(`/api/pokesearch/${this.pokeSearch}`).then(res => res.json()).then(data=> {
                this.pokemonDisplay = data;
            })

        },
        pokePage : function(x){
            let check = Number(x.target.value);

            if(check === 1){
                this.pokemonDisplay= this.pokemon.slice(0,25);
            } else{
                this.pokemonDisplay = this.pokemon.slice(25*check,25*(check+1))
            }

            
            }
            
        
    },
    

    created: function(){
        fetch('api/farm_manage/${farm.id}')
        .then(res => res.json())
        .then(data => {this.zones = data})
        
    }, 
    mounted: function(){
            if( this.csrfToken){
            } else{
                console.log('no token')
            }
        },
    watch: function(pokemon){
            this.$forceUpdate();
        }
}).mount('#app')