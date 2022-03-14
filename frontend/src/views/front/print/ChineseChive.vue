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
        hk: '韭菜',
        en: 'Chinese Chive',
      },
    };
  },
  components: {
    PrintMsg,
  },
  methods: {
    print() {
      const path = 'http://127.0.0.1:5000/chinese-chive';
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
