
app.directive('imageInput', function() {
    return {
        restrict: 'E',
        transclude: true,
        scope: { ngModel: '=', btnStyle: '@' },
        templateUrl: 'app/image-input/image-input.html',
        css: 'app/image-input/image-input.css',

        controller: function($scope) {
            var config = {
                width: 256, height: 256
            };

            function bind(image) {
                $scope.ngModel = image.toDataURL();
                $scope.$apply();
            }

            function crop(image) {
                SmartCrop.crop(image, config, function(result) {
                    var crop = result.topCrop;
                    var canvas = document.createElement('canvas');
                    var ctx = canvas.getContext('2d');

                    canvas.width = config.width;
                    canvas.height = config.height;

                    ctx.drawImage(image,
                        crop.x, crop.y, crop.width, crop.height,
                        0, 0, canvas.width, canvas.height);

                    bind(canvas);
                });
            }

            $scope.update = function(element) {
                var file = element.files[0];

                loadImage.parseMetaData(file, function(data) {
                    loadImage(file, crop, {
                        orientation: data.exif? data.exif.get('Orientation') : null
                    });
                });
            }
        }
    };
});
