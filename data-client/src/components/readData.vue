<template>
  <div class="hello">
    <p>We about to read a lot of data</p>
    <p v-for="(el, index) in getIncidentNumber" :key="index">Incident Number: {{el}}</p>
  </div>
</template>

<script>
import {mapGetters, mapActions} from 'vuex'
export default {
  name: 'readData',
  props: {
    msg: String
  },
  created(){
    this.getData();
  },
  computed: {
    ...mapGetters(
      [
        'getIncidentNumber'
      ]
    )

  },
  mounted(){
    console.log(this.getIncidentNumber);
  },
  methods: {
    ...mapActions(
      [
        'storeDataIntoState'
      ]
    ),
    getData(){
      axios.get('http://localhost:3030/df-head-90')
      .then((resp)=>{
        this.storeDataIntoState(resp.data);
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
