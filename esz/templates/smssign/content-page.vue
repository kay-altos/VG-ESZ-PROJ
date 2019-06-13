
<template>
<div v-show="this.$root.$data.viewContentContainer">
<div id="wrap-app">
<div class="container shadow p-3 mb-5 bg-white rounded">
   <div class="row" >
      <div class="col">
         <form-wizard @on-complete="this.$root.onComplete">
            <tab-content title="Ознакомление" icon="ti-user">
                <fieldset v-if="this.$root.$data.results.Contract">
                <hr />
                <h1><span style="font-family:Arial,Helvetica,sans-serif">Здравствуйте, _{ this.$root.$data.results.Contract.applicant.FullName }!</span></h1>
                <div v-html="this.$root.$data.results.PageGreet.SConstValue"></div>
                <p><span style="font-family:Arial,Helvetica,sans-serif"><span style="font-size:14px"><strong>Сведения о программе</strong></span></span></p>
                <p><span style="font-family:Arial,Helvetica,sans-serif"><span style="font-size:14px"><strong>Код прграммы:</strong> _{ this.$root.$data.results.Contract.program.Code }</span></span></p>
                <p><span style="font-family:Arial,Helvetica,sans-serif"><span style="font-size:14px"><strong>Наименование программы:</strong>&nbsp;_{ this.$root.$data.results.Contract.program.Name }</span></span></p>
                <p><span style="font-family:Arial,Helvetica,sans-serif"><span style="font-size:14px"><strong>Учреждение:</strong>&nbsp;ГБПОУ &laquo;Воробьёвы Горы&raquo; - _{ this.$root.$data.results.Center.Name }  </span></span></p>
                <p><span style="font-family:Arial,Helvetica,sans-serif"><span style="font-size:14px"><strong>Адрес:</strong>&nbsp; _{ this.$root.$data.results.Center.Address } </span></span></p>
                <p><span style="font-family:Arial,Helvetica,sans-serif"><span style="font-size:14px"><strong>Описание программы: </strong>_{ this.$root.$data.results.Contract.program.Description }</span></span></p>
                <hr />
                <p style="text-align:center"><span style="font-size:18px"><span style="font-family:Arial,Helvetica,sans-serif"><strong>Сведения о занятиях</strong></span></span></p>
                <p><span style="font-family:Arial,Helvetica,sans-serif"><span style="font-size:14px"><strong>Дата начала занятий:</strong> _{ this.$root.$data.results.Contract.LessonBeginDate }</span></span></p>
                <p><span style="font-family:Arial,Helvetica,sans-serif"><span style="font-size:14px"><strong>Этап обучения: </strong>начинающий</span></span></p>
                <p><span style="font-family:Arial,Helvetica,sans-serif"><span style="font-size:14px"><strong>Заявление подается:</strong> законным представителем ребенка</span></span></p>
                <hr />
                <p style="text-align:center"><span style="font-family:Arial,Helvetica,sans-serif"><span style="font-size:18px"><strong>Сведения о законном представителе<br />
                   (строго согласно документу, удостоверяющему личность)</strong></span></span>
                </p>
                <applicantpasport-edit></applicantpasport-edit>
                <hr />
                <p style="text-align:center"><span style="font-family:Arial,Helvetica,sans-serif"><span style="font-size:18px"><strong>Сведения о будущем обучающемся<br />
                   (строго согласно документу, удостоверяющему личность)</strong></span></span>
                </p>
                <applicantpasport-edit v-if="this.$root.$data.results.Contract"></applicantpasport-edit>
                <hr />
             </fieldset>
            </tab-content>
            <tab-content title="Согласие" icon="ti-settings">
              <div id="contract-list">
                <contract-container></contract-container>
              </div>
              <div class="clearfix"></div>
              <div id='wrap-sogl' style="margin-top:10px;">
              <form>
                <div class="contr-sogl-elem">
                <div class="form-check">
                  <input type="checkbox" class="form-check-input" id="exampleCheck1">
                  <label class="form-check-label" for="exampleCheck1">Согласие на обработку персональных данных</label>
                  <div class="card">
                    <div class="card-body">
                      <p class="text-justify">
                      «Заказчик» при заключении настоящего договора дает согласие за себя и «Обучающегося» на обработку своих персональных данных «Исполнителем» в соответствии Федеральным законом "О персональных данных" от 27.07.2006 № 152-ФЗ.
                    </p>
                    </div>
                  </div>
                </div>
                </div>
                <div class="contr-sogl-elem">
                <div class="form-check">
                  <input type="checkbox" class="form-check-input" id="exampleCheck1">
                  <label class="form-check-label" for="exampleCheck1">Согласие на подписание договора простой электронной подписью</label>
                  <div class="card">
                    <div class="card-body">
                    <p class="text-justify">
                    В соответствии с федеральным законом от 06.04.2011 N 63-ФЗ «Об электронной подписи» договор будет подписан простой электронной подписью. Код подтверждения будет отправлен на номер телефона, который вы укажете при регистрации. Договор получит уникальный номер и будет отправлен вам на почту, которую вы укажете при регистрации. Вы обязуетесь указать корректные полные регистрационные данные. Вы обязуетесь соблюдать конфиденциальность полученного кода.
                  </p>
                    </div>
                  </div>
                </div>
                </div>
              </form>
              </div>
            </tab-content>
            <tab-content title="Подтверждение" icon="ti-check"></tab-content>
         </form-wizard>
      </div>
   </div>
</div>
</div>

</div>
</template>

<script>
export default {
  name: 'ContentPage',
  delimiters: ['_{', '}'],
  props: [],
  data(){
    return {

    }
  },
  components: {

  }
}

</script>
