<template>
  <div>
    <h1>예매할 티켓 정보 입력하기</h1>

    <v-form v-on:submit.prevent="submit">
      <v-container fluid>
        <v-row align="center">
          <v-row align="center">
            <v-radio-group v-model="logintype" :mandatory="true" row>
              <v-radio label="회원번호" value="1"></v-radio>
              <v-radio label="인증된 휴대전화번호" value="3"></v-radio>
            </v-radio-group>
          </v-row>

          <v-row align="center">
            <v-col class="d-flex" cols="12" sm="6">
              <v-text-field v-model="srtid" label="SRT ID"></v-text-field>
            </v-col>

            <v-col class="d-flex" cols="12" sm="6">
              <v-text-field v-model="srtpw" label="SRT 비밀번호"></v-text-field>
            </v-col>
          </v-row>

          <v-row align="center">
            <v-col class="d-flex" cols="12" sm="6">
              <v-text-field v-model="phone" label="예약 완료시 연락받을 번호"></v-text-field>
            </v-col>
          </v-row>

          <v-row align="center">
            <v-select :items="dpt" label="출발지" solo></v-select>
            <v-select :items="arr" label="도착지" solo></v-select>
          </v-row>

          <v-row align="center">
            <v-select :items="adult" label="어른 인원" solo></v-select>
            <v-select :items="child" label="아이 인원" solo></v-select>
          </v-row>

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
      srtid: "",
      srtpw: "",
      logintype: "",
      dpt: [
        "수서",
        "동탄",
        "지제",
        "천안안산",
        "오송",
        "대전",
        "김천(구미)",
        "동대구",
        "신경주",
        "울산(통도사)",
        "부산",
        "공주",
        "익산",
        "정읍",
        "광주송정",
        "나주",
        "목포"
      ],
      arr: [
        "수서",
        "동탄",
        "지제",
        "천안안산",
        "오송",
        "대전",
        "김천(구미)",
        "동대구",
        "신경주",
        "울산(통도사)",
        "부산",
        "공주",
        "익산",
        "정읍",
        "광주송정",
        "나주",
        "목포"
      ],
      adult: [1, 2, 3, 4, 5, 6, 7],
      child: [1, 2, 3, 4, 5, 6, 7],
      date: "",
      dptime: "",
      ticketnum: "",
      phone: ""
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
