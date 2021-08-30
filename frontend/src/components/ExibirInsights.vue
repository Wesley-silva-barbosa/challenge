<template>
  <div class="exibir">
    <v-img
      height="300px"
      src="https://resources-live.sketch.cloud/files/1921a379-ce65-48a0-aa3c-a7f8d339fd9f.png?Expires=1630202400&Signature=irANUjzMe2JiPStbZG~N8a3OmCaYrJzEOPqZ2eJKakspS9qootyVykLNdPbAIkWgiDarE9fwV0tAvGlQZhyPD3hdlsdpY-HUoy9PRBkTF8~mmaV1jHyHH8b5dv1hZLFEPLOl47U~O1XsrBKDpeWT-cLVyzLs74sIOyPxX5puUlU_&Key-Pair-Id=APKAJOITMW3RWOLNNPYA"> 
    </v-img>

    <div id="cabecalho">     
      <router-link id="rota_criarInsights" to="/create"> + </router-link>
      <div id="icon"></div>
      <v-avatar id="avatar" size="56">
        <v-card-title class="white--text">
          <img alt="user" src="../assets/wesley-foto.jpg">
        </v-card-title>
      </v-avatar>

      <p id="usuario" class="ml-3">
           Olá, {{ user }}!
      </p>
      <p id="email">
        {{ email }}
      </p>
      
    </div>
    
    <v-card-text id="conteudo-card">
      <div id="feed" class="font-weight-bold ml-8 mb-2">
          Feed de <strong> Insights</strong>
      </div>

      <v-card id="cards-menu" v-for="insight in insights" :key="insight.id">
        <div class="font-weight-normal">
          <strong>{{ insight.descricao }}</strong>
          <br/>
          <v-btn v-if="insight.categoria" outlined id="categoria">
            {{ insight.categoria }}
          </v-btn>
                  
          <div>
            {{ insight.insight }}
          </div>
        </div>
      </v-card>
    </v-card-text>
        <button @click="getInsights(true)">
          <div id="mais">
          <div class="dots">
              <div class="dot"></div>
              <div class="dot"></div>
              <div class="dot"></div>
          </div>
        
        Toque para exibir mais insights
      
      </div>
        </button>

       <span @click="search(word)" class="material-icons">
        search
       </span>
      
      <v-text-field
          v-model="word"
          placeholder="Pesquise por termos ou categorias…"
          solo>  
      </v-text-field>
        
  </div>
</template>

<script>
import axios from "axios";

  export default {
    name: 'Home',
     props: {
       msg: String
  },
    data: () => ({
      user: "Wesley",
      email: "mix.ottony@gmail.com",
      insights: [],
      items: [], 
      word: ""
    }),
    methods: {
      getInsights(more){
        let config = {
          headers: {
            accept: "application/json",
            "Content-Type": "application/json",
          }
        };

        const params = {
          skip: more? this.insights.length : 0 ,
          limit: more? 1:4
        };
     
        axios
          .get(process.env.VUE_APP_API+`${params.skip}/${params.limit}`, config)
          .then((result) => {
          
          more ? this.insights.push(result.data[0]) : this.insights = result.data;
      
          })
          .catch((err) => {
            console.log(err);
          });
      },
      search(word){
         let config = {
          headers: {
            accept: "application/json",
            "Content-Type": "application/json",
          }
        };
     
        axios
          .get(process.env.VUE_APP_API+`${word}`, config)
          .then((result) => {
          
          this.insights = result.data;
      
          })
          .catch((err) => {
            console.log(err);
          });
      }
    },
    mounted() {
      this.getInsights(false);
    }       
  }
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:ital@1&display=swap');

#icon {
  background-image: url("../assets/brand-insights@3x.svg");
  background-size: contain;
  background-position: center center;
  width: 46px;
  height: 46px;
  margin-left: 16px;
  float: left;
}

.exibir {
background: #F4F4F4;
}

#usuario {
  font-family: system-ui;
  font-weight: 325;
  color: #ececece7;
  font-style: italic;
  font-size: 25px; 
}

.white--text {
  align-items: center;
}

#categoria {
  font-family: fantasy;
  font-size: xx-small;
  border-radius: 5px;
  color:#ED4D77;
  Width: 77;
  Height: 28;
  padding: 10px;
  margin: 18px;
  margin-top: 10px;
}

#feed {
  color:#ED4D77;
  font-size: 20px;
  font-style: italic;
  padding: 1px;
  position: relative;
  top: -17px;
}

#cards-menu {
  padding-top: 10px;
  margin-top: 10px;
  border-radius: 8px;
}

#conteudo-card {
  position: relative;
  top: -250px;
}

#cabecalho {
  position: relative;
  top: -290px;
}

#avatar {
border: solid;
color:#ED4D77;
right: 2pc;
}

#rota_criarInsights {
   font-weight: 600;
   color: #ED4D77;
   padding-left:90%;
   text-decoration: none;
   font-family: emoji;
   font-size: xx-large;
   position: relative;
   top: 40px;
 }

 #rota_home {
   font-weight: 600;
   color: #ED4D77;
   padding-right:80%;
 }
 
 #email {
      color: #f4f4f49d;
    font-size: 11px;
    font-family: 'Space Mono', monospace;
    font-style: italic;
    font-weight: 500;
 }

 #mais {
   color: #666666;
   font-size: 14px;
   font-weight: 500;
   font-family: system-ui;
   position: relative;
   top: -200px;
   justify-content: center;
   align-items: center; 
   display: flex; 
   flex-direction: column
 }

 .dot {
  width: 7px;
  height: 7px;
  background-color: #4444;
  border-radius: 50%;
}

.dots {
  display: flex;
  flex-direction: row;
  padding-top: 10px;
  padding-bottom: 15px;
  width: 30px;
  justify-content: space-between;
}

.material-icons {
  z-index: 1;
  top: 70px;
  left: 20%;
  background: white;
  position: relative;
  cursor: pointer;
}

</style>
