Vue.use(VueFormWizard);

var BaseUrl = "http://dev.esz.dvorec.net";
var currentUrl;
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';

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


Vue.component('student-edit', {
          delimiters: ['_{', '}'],
          props: ['name'],
         data() {
           return {
             value: '{}',
             studentName: '{{ cce_stud.Name }}',
             studentBd: '{{ cce_stud.DateBirth | date:"Y-m-d" }}',
             studentGl: '{{ cce_stud.GenderLabel }}',
             studentDocumentType: '{{ cce_stud.DocumentType }}',
             studentDocumentNumber: '{{ cce_stud.SeriaNumDoc }}',
             studentDocumentDateOut: '{{ cce_stud.DatarRegDoc | date:"Y-m-d" }}',
             tempstudentName: null,
             tempstudentBd: null,
             tempstudentGl: null,
             tempstudentDocumentType: null,
             tempstudentDocumentNumber: null,
             tempstudentDocumentDateOut: null,
             editing: false

             }
         },
          template:`
          <div>
             <div v-if="!editing">
               <p>
             <span style="font-family:Arial,Helvetica,sans-serif">
               <strong>ФИО обучающегося: </strong>_{ studentName }
             </span>
           </p>
              <p>
             <span style="font-family:Arial,Helvetica,sans-serif">
               <strong>Пол:</strong> _{ studentGl }
             </span>
           </p>
              <p>
             <span style="font-family:Arial,Helvetica,sans-serif">
               <strong>Дата рождения:</strong> _{ studentBd }
             </span>
           </p>
              <!--p>
             <span style="font-family:Arial,Helvetica,sans-serif">
               <strong>Тип документа удостоверяющего личность: &nbsp;</strong>_{ studentDocumentType }
             </span>
           </p-->
              <p>
             <span style="font-family:Arial,Helvetica,sans-serif">
               <strong>Номер документа удостоверяющего личность: &nbsp;</strong>_{ studentDocumentNumber }
             </span>
           </p>
              <p>
             <span style="font-family:Arial,Helvetica,sans-serif">
               <strong>Дата выдачи документа удостоверяющего личность: &nbsp;</strong>_{ studentDocumentDateOut }
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
                     <strong>ФИО обучающегося:</strong>
                       <input type="text" class="form-control" v-model="tempstudentName" maxlength="180">
                   </span>
                 </span>
               </p>
                   </div>
                   <div class="form-group">
                      <p>
                 <span style="font-family:Arial,Helvetica,sans-serif">
                   <span style="font-size:14px">
                     <strong>Пол:</strong>
                     <input type="text" class="form-control" v-model="studentGl" maxlength="180">
                   </span>
                 </span>
               </p>
                   </div>
                   <div class="form-group">
                      <p>
                 <span style="font-family:Arial,Helvetica,sans-serif">
                   <span style="font-size:14px">
                     <strong>Дата рождения:</strong>
                     <input  type="date" class="form-control" v-model="tempstudentBd">
                   </span>
                 </span>
               </p>
                   </div>
                   <div class="form-group">
                      <!--p>
                 <span style="font-family:Arial,Helvetica,sans-serif">
                   <span style="font-size:14px">
                     <strong>Тип документа удостоверяющего личность:</strong>
                     <select class="form-control" v-model="tempstudentDocumentType">
                       <option value="Метрика">Метрика</option>
                       <option value="СНИЛС">СНИЛС</option>
                     </select>
                   </span>
                 </span>
               </p-->
                   </div>
                   <div class="form-group">
                      <p>
                 <span style="font-family:Arial,Helvetica,sans-serif">
                   <span style="font-size:14px">
                     <strong>Номер документа удостоверяющего личность:</strong>
                       <input type="text" class="form-control" v-model="tempstudentDocumentNumber" maxlength="11">
                   </span>
                 </span>
               </p>
                   </div>
                   <div class="form-group">
                      <p>
                 <span style="font-family:Arial,Helvetica,sans-serif">
                   <span style="font-size:14px">
                     <strong>Дата выдачи документа удостоверяющего личность:</strong>
                      <input type="date" v-model="tempstudentDocumentDateOut" class="form-control"/>
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

            enableEditing: function(e){
              //console.log(e.target.getAttribute('value'))
              this.tempstudentName = this.studentName;
              this.tempstudentBd = this.studentBd;
              this.tempstudentGl = this.studentGl;
              this.tempstudentDocumentType = this.studentDocumentType;
              this.tempstudentDocumentNumber = this.studentDocumentNumber;
              this.tempstudentDocumentDateOut = this.studentDocumentDateOut;
              this.editing = true;
         },
          disableEditing: function(){
            this.tempstudentName = null;
            this.tempstudentBd = null;
            this.tempstudentGl  = null;
            this.tempstudentDocumentType = null;
            this.tempstudentDocumentNumber = null;
            this.empstudentDocumentDateOut = null;
            this.editing = false;
            },
          saveEdit: function(){
            // However we want to save it to the database
            this.studentName = this.tempstudentName;
            this.studentBd = this.tempstudentBd;
            this.studentGl = this.tempstudentGl;
            this.studentDocumentType = this.tempstudentDocumentType;
            this.studentDocumentNumber = this.tempstudentDocumentNumber;
            this.studentDocumentDateOut = this.tempstudentDocumentDateOut;

           axios.post(BaseUrl + currentUrl, {
              'action': 'saveStudent',
              'Name': this.studentName,
              'DateBirth': this.studentBd,
              //'DocumentType': this.studentDocumentType,
              'SeriaNumDoc': this.studentDocumentNumber,
              'DatarRegDoc': this.studentDocumentDateOut,
              'GenderLabel': this.studentGl
           })
              .then((response) => {
                console.log(response);
               window.location.href = window.location.href;

              })
              .catch((error) => {
                console.log(error);
              });

            this.disableEditing();
         }
         }


         })


Vue.component('applicantpasport-edit', {
 delimiters: ['_{', '}'],
 props: ['name'],
data() {
  return {
    value: '{{ ApplicantPhone.Phone }}',
    applicantphone: '{{ ApplicantPhone.Phone }}',
    applicantemail: '{{ ApplicantEmail.Email }}',
    applicantFullname: '{{ ContractObj.Contract.Applicant.FullName }}',
    applicantid: '{{ ContractObj.Contract.Applicant.id }}',
    ApplicantDocWhomWhenIssued: '{{ ApplicantPassp.ApplicantDocWhomWhenIssued }}',
    ApplicantAddress: '{{ ApplicantPassp.ApplicantAddress }}',
    SerialPaspDoc: '{{ ApplicantPassp.SerialPaspDoc }}',
    NumPaspDoc: '{{ ApplicantPassp.NumPaspDoc }}',
    DataOutDoc: '{{ ApplicantPassp.DataOutDoc | date:"Y-m-d" }}',
    applicantsnils: '{{ ContractObj.Contract.Applicant.ApplicantSnils }}',
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
         <span class='text' @click="enableEditing($event)">_{  applicantFullname }</span>
       </span>
     </span>
   </p>
     <p>
    <span style="font-family:Arial,Helvetica,sans-serif">
     <span style="font-size:14px">
       <strong>Телефон:</strong>
       <span class='text' @click="enableEditing($event)">_{ applicantphone }</span>
     </span>
   </span>
   </p>
   <p>
     <span style="font-family:Arial,Helvetica,sans-serif">
       <span style="font-size:14px">
         <strong>Электронная почта:</strong>
           <span class='text' @click="enableEditing($event)">_{ applicantemail }</span>
       </span>
     </span>
   </p>
   <p>
     <span style="font-family:Arial,Helvetica,sans-serif">
       <span style="font-size:14px">
         <strong>СНИЛС:</strong>
         <span class='text' @click="enableEditing($event)">_{ applicantsnils }</span>
       </span>
     </span>
   </p>
   <p>
   <span style="font-family:Arial,Helvetica,sans-serif">
     <span style="font-size:14px">
       <strong>Кем и когда выдан:</strong>
         <span class='text' @click="enableEditing($event)">_{  ApplicantDocWhomWhenIssued }</span>
     </span>
   </span>
   </p>
   <p>
     <span style="font-family:Arial,Helvetica,sans-serif">
       <span style="font-size:14px">
         <strong>Адрес регистрации:</strong>
           <span class='text' @click="enableEditing($event)">_{ ApplicantAddress }</span>
       </span>
     </span>
   </p>
   <p>
     <span style="font-family:Arial,Helvetica,sans-serif">
       <span style="font-size:14px">
         <strong>Серия паспорта:</strong>
         <span class='text' @click="enableEditing($event)">_{ SerialPaspDoc }</span>
       </span>
     </span>
   </p>
   <p>
     <span style="font-family:Arial,Helvetica,sans-serif">
       <span style="font-size:14px">
         <strong>Номер паспорта:</strong>
         <span class='text' @click="enableEditing($event)">_{ NumPaspDoc }</span>
       </span>
     </span>
   </p>
   <p>
     <span style="font-family:Arial,Helvetica,sans-serif">
       <span style="font-size:14px">
         <strong>Дата выдачи:</strong>
         <span class='text' @click="enableEditing($event)">_{ DataOutDoc }</span>
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
   enableEditing: function(e){
     //console.log(e.target.getAttribute('value'))
     this.tempApplicantFullname = this.applicantFullname;
     this.tempApplicantphone = this.applicantphone;
     this.tempApplicantemail = this.applicantemail;
     this.tempApplicantDocWhomWhenIssued = this.ApplicantDocWhomWhenIssued;
     this.tempApplicantAddress = this.ApplicantAddress;
     this.tempSerialPaspDoc = this.SerialPaspDoc;
     this.tempNumPaspDoc = this.NumPaspDoc;
     this.tempDataOutDoc = this.DataOutDoc;
     this.tempapplicantsnils = this.applicantsnils;

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
   this.applicantFullname = this.tempApplicantFullname;
   this.applicantphone = this.tempApplicantphone;
   this.applicantemail = this.tempApplicantemail;

   this.ApplicantDocWhomWhenIssued = this.tempApplicantDocWhomWhenIssued;
   this.ApplicantAddress = this.tempApplicantAddress;
   this.SerialPaspDoc = this.tempSerialPaspDoc;
   this.NumPaspDoc = this.tempNumPaspDoc;
   this.DataOutDoc = this.tempDataOutDoc;

  this.applicantsnils =   this.tempapplicantsnils;

   axios.post(BaseUrl + currentUrl, {
     'action': 'saveApplicantPasport',
     'FullName': this.applicantFullname,
     'ApplicantPhone': this.applicantphone,
     'ApplicantEmail': this.applicantemail,

     'ApplicantDocWhomWhenIssued': this.ApplicantDocWhomWhenIssued,
     'ApplicantAddress': this.ApplicantAddress,
     'SerialPaspDoc': this.SerialPaspDoc,
     'NumPaspDoc': this.NumPaspDoc,
     'DataOutDoc': this.DataOutDoc,
     'ApplicantSnils': this.applicantsnils
   })
     .then((response) => {

       console.log(response);
       window.location.href = window.location.href;
     })
     .catch((error) => {
       console.log(error);
     });




   this.disableEditing();
}
}


})

var app = new Vue({
mounted: function(){
  if(localStorage.sIndex == ''){
     localStorage.sIndex = 0;
  }


},
delimiters: ['${', '}'],
el: '#app',
created: function() {
currentUrl = window.location.pathname;
console.log(currentUrl);
},
data: {
  value: 'Click Me!',
scrld: false,
results: [],
showModal: false,
vsmsCode: '',
ContractSignTransactionState_id : {{ ContractSignTransactionState.id }},
ContractSignTransactionState_lable :"{{ ContractSignTransactionState.SatateLabel }}"
},
methods: {
onComplete: function(){
 alert('Yay. Done!');
},
handleScroll: function (evt, el) {
        var container = this.$el.querySelector("#container");
            if (container.scrollTop+container.offsetHeight == container.scrollHeight){
              this.$parent.$data.scrld = true;
            }
 },
getSmsCode: function (event) {
 axios.post(BaseUrl + currentUrl, {'action': 'SendSmsSign'})
   .then((response) => {

     this.ContractSignTransactionState_id = response.data.csts_id;
     this.ContractSignTransactionState_lable = response.data.csts_lable;

     console.log(response);
   })
   .catch((error) => {
     console.log(error);
 });
},
verifySmsCode: function (event, data) {
 axios.post(BaseUrl + currentUrl, {'action': 'verifyCode', 'vsmsCode': this.vsmsCode})
   .then((response) => {
     this.ContractSignTransactionState_id = response.data.csts_id;
     this.ContractSignTransactionState_lable = response.data.csts_lable;
     console.log(response);
   })
   .catch((error) => {
     console.log(error);
 });
}
}
});
