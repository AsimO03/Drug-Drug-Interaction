<template>
  <div id="app">
    <h1>DRUG-DRUG-INTERACTIONS</h1>
    <div id="selectedDrugsDiv" style="display: flex; align-items: baseline;">
      <h5>Drugs:&nbsp</h5>
      <p v-for="(drug, count) in selectedDrugs" :key="count" >{{drug}} &nbsp</p>
    </div>
    

    <b-form-input v-model="drug" @keyup.enter="addDrug" placeholder="Enter drug names to see the interactions" style="width: 80%;"></b-form-input>
    <button type="button" class="btn btn-dark" @click="addDrug" style="margin-top: 10px; width: 300px;">Add drug</button>
    <button type="button" class="btn btn-dark" @click="seeResult" style="margin-top: 10px; width: 300px; height: 100px;">See the Result</button>
    
    <h2 style="margin-top: 20px;">{{result}}</h2>

    <div></div>
  </div>
</template>

<script>

export default {
  name: 'app',
  components: {
  },
  data(){
    return{
      selectedDrugs: [],
      drug: '',
      result: '',
    }
  },
  mounted(){
    console.log("mounted");
  },
  methods:{
    addDrug() {
      if(this.drug != ''){
        this.selectedDrugs.push(this.drug)
        this.drug = ''
      }else{
        alert("The Input is empty")
      }
    },
    seeResult(){
      this.result = "No Results found"
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

#selectedDrugsDiv{
  display: flex;
  justify-content: center;
  align-items: baseline;
}
</style>
