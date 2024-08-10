<template>
  <div class="blog-generator">
    <h1>AI Blog Generator</h1>
    <form @submit.prevent="generateBlog">
      <div class="form-group">
        <label for="prompt">Blog Topic:</label>
        <input
          type="text"
          id="prompt"
          v-model="prompt"
          required
          placeholder="Enter a topic for the blog..."
        />
      </div>
      <div class="form-group">
        <label for="max-length">Maximum Length:</label>
        <input
          type="number"
          id="max-length"
          v-model.number="maxLength"
          min="50"
          max="500"
          placeholder="100"
        />
      </div>
      <button type="submit">Generate Blog</button>
    </form>

    <div v-if="loading" class="loading">
      <p>Generating blog content...</p>
    </div>

    <div v-if="blogContent" class="blog-content">
      <h2>Generated Blog Content</h2>
      <p>{{ blogContent }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      prompt: '',
      maxLength: 100,
      blogContent: '',
      loading: false,
      error: null,
    };
  },
  methods: {
    async generateBlog() {
      this.loading = true;
      this.blogContent = '';
      this.error = null;
      try {
        const response = await axios.post(`${process.env.VUE_APP_BACKEND_URL}/generate`, {
          prompt: this.prompt,
          max_length: this.maxLength,
        });
        this.blogContent = response.data.blog_content;
      } catch (error) {
        this.error = 'An error occurred while generating the blog content.';
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>

<style scoped>
.blog-generator {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
}

.form-group {
  margin-bottom: 20px;
}

button {
  padding: 10px 20px;
  background-color: #42b983;
  color: white;
  border: none;
  cursor: pointer;
}

button:hover {
  background-color: #369f75;
}

.loading {
  text-align: center;
  margin-top: 20px;
}

.blog-content {
  margin-top: 30px;
  padding: 15px;
  background-color: #f9f9f9;
  border: 1px solid #ddd;
  border-radius: 5px;
}
</style>
