
app.controller('notifications', function($scope, $timeout) {

    $scope.notifications_list = [
        { type    : "INVITATION",
          sender  : "Someone",
          mensage : "mensage",
          url_img : "https://40.media.tumblr.com/20625bfafa453b4d628f7de4a5d7e14e/tumblr_nz7u21Qai41t4osjeo2_250.png",
          comment : "O bigu foi tão bom que me emocionei.."},

        { type    : "INVITATION",
          sender  : "Someone",
          mensage : "mensage",
          url_img : "https://pbs.twimg.com/profile_images/435830531951837184/Z50DeEtx.jpeg",
          comment : "O bigu foi tão bom que me emocionei.."},

        { type    : "INVITATION",
          sender  : "Someone",
          mensage : "mensage",
          url_img : "https://40.media.tumblr.com/20625bfafa453b4d628f7de4a5d7e14e/tumblr_nz7u21Qai41t4osjeo2_250.png",
          comment : "O bigu foi tão bom que me emocionei.."}
    ];

    $scope.delete = function(index) {
        $scope.notifications_list.splice(index, 1);
    }
});
