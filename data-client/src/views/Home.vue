<template>
  <div class="home">
    <read-data></read-data>
  </div>
</template>

<script>
// @ is an alias to /src
import readData from '@/components/readData.vue'

export default {
  name: 'home',
  components: {
    readData
  }
}
</script>
