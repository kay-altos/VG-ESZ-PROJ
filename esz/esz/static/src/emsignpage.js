
      //const state = { steps: 3, step: undefined }
      //import { VStepper } from 'vue-stepper-component'
      Vue.use(VueLoading);
      Vue.use(VStepper);
      Vue.component('loading', VueLoading);


      var BaseUrl = "http://dev.esz.dvorec.net";
      var currentUrl;

      axios.defaults.xsrfCookieName = 'csrftoken';
      axios.defaults.xsrfHeaderName = 'X-CSRFToken';
      axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
/*
      Vue.component('content-page', {
        delimiters: ['_{', '}'],
        props: [],
        //v-if="this.$root.$data.results.Contract"
        //this.$root.$data.results.
        //v-show="this.$root.$data.viewContentContainer"
        template: `
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
        `
      })
*/

      Vue.component('applicantpasport-edit', {
       delimiters: ['_{', '}'],
       props: ['name'],
       computed: {
         setBut1(){
            if (this.$root.$data.results.Contract.applicant.ApplicantSnils == ''){
              $("#ttt").attr("disabled", true);
            }

         }
       },
       mounted: function(){
         var self = this;
         this.setBut();

       },
      data() {
        return {
          results : this.$root.$data.results,
          tempapplicantsnils: null,
          tempApplicantphone: null,
          tempApplicantemail: null,
          tempApplicantFullname: null,
          tempApplicantDocWhomWhenIssued: null,
          tempApplicantAddress: null,
          tempSerialPaspDoc: null,
          tempNumPaspDoc: null,
          tempDataOutDoc: null,
          editing: false

            }
          },
       template:`
       <div>
        <div v-if="!editing">
             <p>
           <span style="font-family:Arial,Helvetica,sans-serif">
             <span style="font-size:14px">
               <strong>ФИО Заявителя:</strong>
               <span class='text' @click="enableEditing($event)">_{  results.Contract.applicant.FullName }</span>
             </span>
           </span>
         </p>
           <p>
          <span style="font-family:Arial,Helvetica,sans-serif">
           <span style="font-size:14px">
             <strong>Телефон:</strong>
             <span class='text' @click="enableEditing($event)">_{  results.ApplicantPhone.Phone }</span>
           </span>
         </span>
         </p>
         <p>
           <span style="font-family:Arial,Helvetica,sans-serif">
             <span style="font-size:14px">
               <strong>Электронная почта:</strong>
                 <span class='text' @click="enableEditing($event)">_{  results.ApplicantEmail.Email }</span>
             </span>
           </span>
         </p>
         <p>
           <span style="font-family:Arial,Helvetica,sans-serif">
             <span style="font-size:14px">
               <strong>СНИЛС:</strong>
               <span class='text' @click="enableEditing($event)">_{  results.Contract.applicant.ApplicantSnils }</span>
             </span>
           </span>
         </p>
         <p>
         <span style="font-family:Arial,Helvetica,sans-serif">
           <span style="font-size:14px">
             <strong>Кем и когда выдан:</strong>
               <span class='text' @click="enableEditing($event)">_{  results.ApplicantPassp.ApplicantDocWhomWhenIssued }</span>
           </span>
         </span>
         </p>
         <p>
           <span style="font-family:Arial,Helvetica,sans-serif">
             <span style="font-size:14px">
               <strong>Адрес регистрации:</strong>
                 <span class='text' @click="enableEditing($event)">_{ results.ApplicantPassp.ApplicantAddress }</span>
             </span>
           </span>
         </p>
         <p>
           <span style="font-family:Arial,Helvetica,sans-serif">
             <span style="font-size:14px">
               <strong>Серия паспорта:</strong>
               <span class='text' @click="enableEditing($event)">_{ results.ApplicantPassp.SerialPaspDoc }</span>
             </span>
           </span>
         </p>
         <p>
           <span style="font-family:Arial,Helvetica,sans-serif">
             <span style="font-size:14px">
               <strong>Номер паспорта:</strong>
               <span class='text' @click="enableEditing($event)">_{ results.ApplicantPassp.NumPaspDoc }</span>
             </span>
           </span>
         </p>
         <p>
           <span style="font-family:Arial,Helvetica,sans-serif">
             <span style="font-size:14px">
               <strong>Дата выдачи:</strong>
               <span class='text' @click="enableEditing($event)">_{ results.ApplicantPassp.DataOutDoc }</span>
             </span>
           </span>
         </p>
         <div style="max-width: 170px; margin-left: auto;  margin-right: 0;"><input class="btn btn-info" @click="enableEditing()" type="button" value="Изменить сведения" /></div>
          </div>
          <div v-if="editing">
             <form>
                <div class="form-group">
                   <p>
               <span style="font-family:Arial,Helvetica,sans-serif">
                 <span style="font-size:14px">
                   <strong>ФИО Заявителя:</strong>
                   <input type="text" class="form-control" v-model="tempApplicantFullname" maxlength="180">
                 </span>
               </span>
             </p>
                </div>
                <div class="form-group">
                   <p>
               <span style="font-family:Arial,Helvetica,sans-serif">
                 <span style="font-size:14px">
                   <strong>Телефон:</strong>
                   <input type="text" v-model="tempApplicantphone" class="form-control" maxlength="12"/>
                 </span>
               </span>
             </p>
                </div>
                <div class="form-group">
                   <p>
               <span style="font-family:Arial,Helvetica,sans-serif">
                 <span style="font-size:14px">
                   <strong>Электронная почта:</strong>
                     <input type="email" v-model="tempApplicantemail" class="form-control" maxlength="150">
                 </span>
               </span>
             </p>
                </div>
                <div class="form-group">
                   <p>
               <span style="font-family:Arial,Helvetica,sans-serif">
                 <span style="font-size:14px">
                   <strong>СНИЛС:</strong>
                   <input maxlength="11" v-model="tempapplicantsnils" class="form-control"/>
                 </span>
               </span>
             </p>
                </div>
                <div class="form-group">
                   <p>
               <span style="font-family:Arial,Helvetica,sans-serif">
                 <span style="font-size:14px">
                   <strong>Кем и когда выдан:</strong>
                   <textarea class="form-control" v-model="tempApplicantDocWhomWhenIssued" maxlength="1024" rows="3"></textarea>
                 </span>
               </span>
             </p>
                </div>
                <div class="form-group">
                   <p>
               <span style="font-family:Arial,Helvetica,sans-serif">
                 <span style="font-size:14px">
                   <strong>Адрес регистрации:</strong>
                   <input v-model="tempApplicantAddress" maxlength="1024" class="form-control"/>
                 </span>
               </span>
             </p>
                </div>
                <div class="form-group">
                   <p>
               <span style="font-family:Arial,Helvetica,sans-serif">
                 <span style="font-size:14px">
                   <strong>Серия паспорта:</strong>
                   <input v-model="tempSerialPaspDoc" maxlength="4" class="form-control"/>
                 </span>
               </span>
             </p>
                </div>
                <div class="form-group">
                   <p>
               <span style="font-family:Arial,Helvetica,sans-serif">
                 <span style="font-size:14px">
                   <strong>Номер паспорта:</strong>
                     <input v-model="tempNumPaspDoc" maxlength="6" class="form-control"/>
                 </span>
               </span>
             </p>
                </div>
                <div class="form-group">
                   <p>
               <span style="font-family:Arial,Helvetica,sans-serif">
                 <span style="font-size:14px">
                   <strong>Дата выдачи:</strong>
                   <input type="date" v-model="tempDataOutDoc" class="form-control"/>
                 </span>
               </span>
             </p>
                </div>
                <div style="max-width: 382px; margin-left: auto;  margin-right: 0;">
             <button style="width: 188px;" class="btn btn-danger" @click="disableEditing"> Отменить изменения </button>
             <button style="width: 188px;" class="btn btn-success" @click="saveEdit"> Сохранить изменения </button>
           </div>
             </form>
          </div>
       </div>
       `,
       methods: {
         setBut: function(){
           var str = this.$root.$data.results.Contract.applicant.ApplicantSnils
            if (this.$root.$data.results.Contract.applicant.ApplicantSnils == null ){
              $("#ttt").attr("disabled", true);
            }else{
              $("#ttt").attr("disabled", false);

            }
          },
         enableEditing: function(e){
           //console.log(e.target.getAttribute('value'))
           this.tempApplicantFullname = this.results.Contract.applicant.FullName;
           this.tempApplicantphone = this.results.ApplicantPhone.Phone;
           this.tempApplicantemail = this.results.ApplicantEmail.Email;
           this.tempApplicantDocWhomWhenIssued = this.results.ApplicantPassp.ApplicantDocWhomWhenIssued;
           this.tempApplicantAddress = this.results.ApplicantPassp.ApplicantAddress;
           this.tempSerialPaspDoc = this.results.ApplicantPassp.SerialPaspDoc;
           this.tempNumPaspDoc = this.results.ApplicantPassp.NumPaspDoc;
           this.tempDataOutDoc = this.results.ApplicantPassp.DataOutDoc;
           this.tempapplicantsnils = this.results.Contract.applicant.ApplicantSnils;

           this.editing = true;

         },
       disableEditing: function(){
         this.tempapplicantsnils = null;
         this.tempApplicantFullname = null;
         this.tempApplicantphone = null;
         this.tempApplicantemail = null;
         this.tempApplicantDocWhomWhenIssued = null;
         this.tempApplicantAddress = null;
         this.tempSerialPaspDoc = null;
         this.tempNumPaspDoc = null;
         this.tempDataOutDoc = null;

         this.editing = false;
         },
       saveEdit: function(){
         // However we want to save it to the database
         this.results.Contract.applicant.FullName = this.tempApplicantFullname;
         this.results.ApplicantPhone.Phone = this.tempApplicantphone;
         this.results.ApplicantEmail.Email = this.tempApplicantemail;

         this.results.ApplicantPassp.ApplicantDocWhomWhenIssued = this.tempApplicantDocWhomWhenIssued;
         this.results.ApplicantPassp.ApplicantAddress = this.tempApplicantAddress;
         this.results.ApplicantPassp.SerialPaspDoc = this.tempSerialPaspDoc;
         this.results.ApplicantPassp.NumPaspDoc = this.tempNumPaspDoc;
         this.results.ApplicantPassp.DataOutDoc = this.tempDataOutDoc;

        this.applicantsnils =   this.tempapplicantsnils;

         axios.post(BaseUrl + currentUrl, {
           data: this.results
         })
           .then((response) => {

             console.log(response);
             this.setBut();
             //window.location.href = window.location.href;
           })
           .catch((error) => {
             console.log(error);
           });


         this.disableEditing();
      }
      }


    });

      Vue.component('contract-container', {
      template: `
       <object data="http://dev.esz.dvorec.net/static/tmpls/htmltplcontracts/{{ userzign }}.html" width="100%" height="500">
       <embed id="contract" src="http://dev.esz.dvorec.net/static/tmpls/htmltplcontracts/{{ userzign }}.html" width="100%" height="500"></embed>
         Error: Embedded data could not be displayed.
         </object>
      `,
      data: {
      //scrld: false,
      },
      created: function  (evt, el) {},
      methods: {
        handleScroll: function (evt, el) {},
         }
      });

      var app = new Vue({

      mounted: function(){
        this.visible = true;
        this.isDisabled = false;
        var self = this;
        axios.get('/api/ct/{{ userzign }}/?format=json')
          .then(function (response) {
              // handle success
              self.results = response.data
            //console.log(self.results);
            })
            .catch(function (error) {
              // handle error
              console.log(error);
            })
            .finally(function () {
                // always executed
            });

      },
      delimiters: ['${', '}'],
      el: '#app',
      components: {
        'content-page': 'content-page.vue',
      },
      data() {
      	return {
          steps: 3,
          step: undefined,
      		results: [],
          isDisabled: false,
          visible: false,
          viewContentContainer: false,
        }
    },
      beforeCreated: function() {

      },
      updated: function() {
      //  $("#wrap-app").css("diaplay: block;");
        this.showEllemAfterPreload();
      },
      created: function() {
      //this.visible = true;
      currentUrl = window.location.pathname;
      this.$refs.rnext1b;

      },

   methods: {
      showEllemAfterPreload: function(){
        var self = this
        setTimeout(function()
        {
          self.viewContentContainer = true;
          self.visible = false;
        }, 1500);


      },
      onComplete: function(){
       alert('Yay. Done!');
      },
      open() {

            console.log('open was clicked, will auto hide');
            let loader = this.$loading.show({
                loader: 'dots'
            });
            setTimeout(() => loader.hide(), 3 * 1000)
        },
        show() {
            console.log('show was clicked, click to hide');
            // do AJAX here
            this.visible = true
        },

      }
      })
