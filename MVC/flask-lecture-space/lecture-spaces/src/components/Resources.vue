<template>
  <div class="box">
    <div class="flex">
      <div class="col-10">
        <h1>Resources</h1>
        <hr><br><br>
        <button type="button" class="button-green small">Add Resource</button>
        <br><br>
        <table class="table-hover">
          <thead>
            <tr>
              <th scope="col">Title</th>
              <th scope="col">Content</th>
              <th scope="col">image</th>
              <th scope="col">rating</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(resource, index) in resources" :key="index">
              <td>{{resource.title}}</td>
              <td>{{resource.content}}</td>
              <td>{{resource.imageUrl}}</td>
              <td>{{resource.rating}}</td>
              <td>
                <div class="button-group" role="group">
                  <button type="button" class="button-yellow small">Update</button>
                  <button type="button" class="button-red small">Delete</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>
<script>
import axios from 'axios';

export default {
  data() {
    return {
      resources: [],
    };
  },
  methods: {
    getResources() {
      const path = 'http://localhost:5001/resources';
      axios.get(path)
        .then((res) => {
          this.resources = res.data.resources;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.getResources();
  },
};
</script>
<style scoped>
.box {
  width: 100%;
  padding-right: 15px;
  padding-left: 15px;
  margin-right: auto;
  margin-left: auto;
}

.flex {
  display: flex;
  flex-wrap: wrap;
  margin-right: -15px;
  margin-left: -15px;
}

.col-10 {
  flex: 0 0 83.333333%;
  max-width: 83.333333%;
  padding-right: 15px;
  padding-left: 15px;
}

.button {
  display: inline-block;
  font-weight: 400;
  text-align: center;
  vertical-align: middle;
  user-select: none;
  border: 1px solid transparent;
  padding: 0.375rem 0.75rem;
  font-size: 1rem;
  line-height: 1.5;
  border-radius: 0.25rem;
  cursor: pointer;
}

.button-green {
  color: #fff;
  background-color: #28a745;
  border-color: #28a745;
}

.small {
  padding: 0.25rem 0.5rem;
  font-size: 0.875rem;
  line-height: 1.5;
  border-radius: 0.2rem;
}

.table-hover {
  width: 100%;
  margin-bottom: 1rem;
  color: white;
  border-collapse: collapse;
}

.table-hover tbody tr:hover {
  color: white;
  background-color: rgba(0, 0, 0, 0.075);
}

th {
  text-align: inherit;
  vertical-align: bottom;
  border-bottom: 2px solid #dee2e6;
}

td {
  padding: 0.75rem;
  vertical-align: top;
  border-top: 1px solid #dee2e6;
}

.button-group {
  display: inline-flex;
  vertical-align: middle;
}

.button-group > .button {
  position: relative;
  flex: 1 1 auto;
}

.button-group > .button:not(:first-child) {
  border-top-left-radius: 0;
  border-bottom-left-radius: 0;
}

.button-group > .button:not(:last-child) {
  border-top-right-radius: 0;
  border-bottom-right-radius: 0;
}

.button-yellow {
  color: #212529;
  background-color: #ffc107;
  border-color: #ffc107;
}

.button-red {
  color: #fff;
  background-color: #dc3545;
  border-color: #dc3545;
}

</style>