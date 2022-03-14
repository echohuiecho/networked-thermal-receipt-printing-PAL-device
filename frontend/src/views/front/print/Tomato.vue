<template lang="">
  <PrintMsg
  :plant="plant"
  >
  </PrintMsg>
</template>
<script>
import PrintMsg from '@/components/PrintMsg.vue';

export default {
  data() {
    return {
      plant: {
        hk: '蕃茄',
        en: 'Tomato',
      },
    };
  },
  components: {
    PrintMsg,
  },
  methods: {
    print() {
      const path = 'http://127.0.0.1:5000/tomato';
      this.$http
        .get(path)
        .then((res) => {
          console.log(res);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  mounted() {
    this.print();
  },
};
</script>
