var jQuery = window.jQuery || django.jQuery;

(function ($) {
  'use strict';

  var colorizeStatus = function () {
    var $status = $('#id_status');
    var $statusLabel = $status.prev('label');

    var updateStatusColor = function (event) {
      $statusLabel.removeClass('blogit-status-0 blogit-status-1 blogit-status-2 blogit-status-3');
      $statusLabel.addClass('blogit-status-' + $status.val());
    };

    $status.on('change', updateStatusColor);
    updateStatusColor();
  };

  $(document).ready(function () {
    colorizeStatus();
  });

})(jQuery);
