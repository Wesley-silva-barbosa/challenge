<template>
  <div id="menu" class="home">
    <ExibirInsights msg="Feed de Insights"/>
  </div>
</template>

<script>
// @ is an alias to /src
import ExibirInsights from '@/components/ExibirInsights.vue'

export default {
  name: 'Home',
  components: {
    ExibirInsights
  }
}
</script>

<style>

</style>