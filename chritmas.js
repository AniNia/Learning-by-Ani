Today=new Date();
var chritmas=new Date(Today.getFullYear(), 11, 25);
if (Today.getMonth()==11 && today.getDate()>25) 
{
chritmas.setFullYear(chritmas.getFullYear()+1); 
}  
var fullday=1000*60*60*24;
console.log(Math.ceil((chritmas.getTime()-Today.getTime())/(fullday))+
" days are left");
