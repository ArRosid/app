<template>
  <div id="app">
    <BlogGenerator />
  </div>
</template>

<script>
import BlogGenerator from './components/BlogGenerator.vue';

export default {
  name: 'App',
  components: {
    BlogGenerator,
  },
};
</script>

<style>
body {
  font-family: Arial, sans-serif;
  background-color: #f4f4f4;
  margin: 0;
  padding: 20px;
}
</style>
