function Pc2JudgeEditBlock(runtime, element) {
  $(element).find('.save-button').bind('click', function() {
    var handlerUrl = runtime.handlerUrl(element, 'studio_submit');
    var data = {
      problemname: $(element).find('input[name=problemname]').val(),
      problemnumber: $(element).find('input[name=problemnumber]').val(),
      allproblem: $(element).find('input[name=allproblem]').val()
    };
    $.post(handlerUrl, JSON.stringify(data)).done(function(response) {
      window.location.reload(false);
    });
  });

  $(element).find('.cancel-button').bind('click', function() {
    runtime.notify('cancel', {});
  });
}
