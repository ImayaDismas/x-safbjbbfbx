$(document).on("pagebeforeshow","#pagetwo",function(){
  alert("pagebeforeshow event fired - pagetwo is about to be shown");
});
$(document).on("pageshow","#pagetwo",function(){
  alert("pageshow event fired - pagetwo is now shown");
});
$(document).on("pagebeforehide","#pagetwo",function(){
  alert("pagebeforehide event fired - pagetwo is about to be hidden");
});
$(document).on("pagehide","#pagetwo",function(){
  alert("pagehide event fired - pagetwo is now hidden");
});