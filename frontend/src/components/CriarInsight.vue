<template>
  <div class="create">
    <v-img id="imagem"
      height="110px"
      src="https://resources-live.sketch.cloud/files/1921a379-ce65-48a0-aa3c-a7f8d339fd9f.png?Expires=1630202400&Signature=irANUjzMe2JiPStbZG~N8a3OmCaYrJzEOPqZ2eJKakspS9qootyVykLNdPbAIkWgiDarE9fwV0tAvGlQZhyPD3hdlsdpY-HUoy9PRBkTF8~mmaV1jHyHH8b5dv1hZLFEPLOl47U~O1XsrBKDpeWT-cLVyzLs74sIOyPxX5puUlU_&Key-Pair-Id=APKAJOITMW3RWOLNNPYA">
    </v-img>

    <div class="row">
      <div class="col-md-1" id="arrow">
        <v-btn class="icons-topo cabecalho" icon to="/"></v-btn>
      </div>
      <div id="cabecalho_criar_insight" class="col-md-10 icons-topo cabecalho">
         CRIAR <strong> INSIGHT</strong>
      </div>
    </div>
    
    <div>
        <div id="criar-descricao">
          <h4 class="main-font">INSIGHT</h4>
          <v-textarea
            placeholder="Escreva aqui o seu insight..."
            height="150"
            v-model="descricao">
          </v-textarea>

          <h4 class="main-font">CATEGORIA</h4>
          <v-textarea
            placeholder="Adicione uma categoria (opcional)..."
            height="100"
            v-model="categoria">
            
          </v-textarea>
        </div>
      </div>
    <br/><br/><br/><br/><br/><br/><br/>
    <v-footer>
      <v-btn block color="secondary" :disabled="!descricao" id="publicar" @click="create">PUBLICAR</v-btn>
    </v-footer>

  </div>
</template>

<script>
import axios from "axios";

require('dotenv').config();

export default {
    name: 'CriarInsight',
    props: {
    msg: String

},
  data:()=>({
    descricao: "",
    categoria: ""

  }),
    methods: {
      create(){
        
        const insight = {
          descricao: this.descricao,
          categoria: this.categoria,
          id:0
        };

        let config = {
          headers: {
            accept: "application/json",
            "Content-Type": "application/json",
          },
        };

        axios
          .post(process.env.VUE_APP_API, insight, config)
          .then((response) => {
        })
        .catch((err) => {
        })
        .finally(() => {
          this.descricao = "";
          this.categoria = "";
        });
      }
    }
}
</script>

<style>

#publicar {
  background: #ED4D77;
  color: #fff;
}

.create {
background: #F4F4F4;
}

.icons-topo {
  color:#ED4D77;
  font-size: 20px;
  font-style: italic;
  padding: 1px;
}

#criar-descricao {
  height: 49vh;
  width: 90vw;
  min-height: 405px;
  max-height: 400px;
  margin-top: 15px;
  margin-inline: auto;
  background-color: #fff;
  border: 1px solid #fff;
  border-radius: 15px;
  padding: 10px;
  position: relative;
  top: -46px;
}

.main-font {
    margin-right: 80%;
    padding: 10px;
    font-style: italic;
}
#criar-categoria {
  height: 49vh;
  width: 90vw;
  min-height: 300px;
  max-height: 400px;
  margin-top: 15px;
  margin-inline: auto;
  background-color: #fff;
  border: 1px solid #fff;
  border-radius: 15px;
  padding: 10px;
}

#arrow{
  background-image: url("../assets/arrow_back_black_24dp.svg");
  background-size: contain;
  background-position: center center;
  width: 26px;
  height: 46px;
  margin-left: 16px;
  float: left;
  cursor: pointer;
}

.cabecalho {
  position: relative;
  display: grid;
}

#cabecalho_criar_insight {
  padding-right: 58px;
}

.row {
    display: flex;
    flex-wrap: nowrap;
    flex: 1 1 auto;
    margin: 0px;
    position: relative;
    top: -70px;    
}

#publicar:disabled {
    background-color: #ed4d7875!important;
    color: white!important;
}

</style>
