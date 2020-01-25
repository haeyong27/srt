<template>
  <div>
    <h1>new form</h1>

    <v-form v-on:submit.prevent="submit">
      <v-container fluid>
        <v-row align="center">
          <v-col class="d-flex" cols="12" sm="6">
            <v-text-field v-model="srtid" label="SRT ID"></v-text-field>
          </v-col>

          <v-col class="d-flex" cols="12" sm="6">
            <v-text-field v-model="srtpw" label="SRT 비밀번호"></v-text-field>
          </v-col>

          <v-col class="d-flex" cols="12" sm="6">
            <v-text-field v-model="logintype" label="logintype"></v-text-field>
          </v-col>

          <v-col class="d-flex" cols="12" sm="6">
            <v-text-field v-model="phone" label="예약 완료시 연락받을 번호"></v-text-field>
          </v-col>

          <v-col class="d-flex" cols="12" sm="6">
            <v-text-field v-model="dpt" label="출발지"></v-text-field>
          </v-col>

          <v-col class="d-flex" cols="12" sm="6">
            <v-text-field v-model="arr" label="도착지"></v-text-field>
          </v-col>

          <v-col class="d-flex" cols="12" sm="6">
            <v-text-field v-model="adult" label="어른 인원"></v-text-field>
          </v-col>

          <v-col class="d-flex" cols="12" sm="6">
            <v-text-field v-model="child" label="아이 인원"></v-text-field>
          </v-col>

          <v-col class="d-flex" cols="12" sm="6">
            <v-text-field v-model="date" label="출발 날짜"></v-text-field>
          </v-col>

          <v-col class="d-flex" cols="12" sm="6">
            <v-text-field v-model="dptime" label="출발하고 싶은 시간"></v-text-field>
          </v-col>

          <v-col class="d-flex" cols="12" sm="6">
            <v-text-field v-model="ticketnum" label="몇시 이후로 몇개"></v-text-field>
          </v-col>
        </v-row>
      </v-container>
      <v-btn @click="submit">등록하기</v-btn>
    </v-form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      srtid: "01021843577",
      srtpw: "Sphv84031!@",
      logintype: "3",
      dpt: "동탄",
      arr: "수서",
      adult: "1",
      child: "0",
      date: "2020-01-18",
      dptime: "14",
      ticketnum: "4",
      phone: "me"
    };
  },
  methods: {
    submit() {
      this.$store.dispatch("post/register_ticket", {
        srtid: this.srtid,
        srtpw: this.srtpw,
        logintype: this.logintype,
        phone: this.phone,
        dpt: this.dpt,
        arr: this.arr,
        adult: this.adult,
        child: this.child,
        date: this.date,
        dptime: this.dptime,
        ticketnum: this.ticketnum
      });
    }
  }
};
</script>
