
app.directive('imageInput', function() {
    return {
        restrict: 'E',
        transclude: true,
        scope: { ngModel: '=', btnStyle: '@' },
        templateUrl: 'app/image-input/image-input.html',
        css: 'app/image-input/image-input.css',

        controller: function($scope) {
            var config = {
                width: 256,
                height: 256
            };

            $scope.update = function(element) {
                var file = element.files[0];
                var reader = new FileReader();

                reader.onload = function() {
                    var image = new Image();
                    image.src = reader.result;

                    SmartCrop.crop(image, config, function(result) {
                        var crop = result.topCrop;
                        var canvas = document.createElement('canvas');

                        canvas.width = config.width;
                        canvas.height = config.height;

                        canvas.getContext('2d').drawImage(image,
                            crop.x, crop.y, crop.width, crop.height,
                            0, 0, canvas.width, canvas.height);

                        $scope.ngModel = canvas.toDataURL();
                        $scope.$apply();
                    });
                };

                reader.readAsDataURL(file);
            }
        }
    };
});
