<template lang="">
  <div>
    <h1> Ping </h1>
    {{ msg }}
  </div>
</template>
<script>
export default {
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    getMessage() {
      const path = 'http://127.0.0.1:5000/ping';
      this.$http
        .get(path)
        .then((res) => {
          console.log(res);
          this.msg = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  mounted() {
    this.getMessage();
  },
};
</script>
