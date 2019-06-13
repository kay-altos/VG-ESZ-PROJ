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
