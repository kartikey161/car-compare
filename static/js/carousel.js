var app = angular.module('mycarousel', []);

app.controller("divdynamic", function ($scope, $http) {
    var data = [
            "http://mwmgraphics.com/REALISTIC_1060/bike_posters/MWM_Bike_Illo_4b.jpg",
            "http://www.woostercollective.com/mattmm2.jpg",
            "http://mwmgraphics.com/TYPOGRAPHY/alphafont_2/mwm_alphafont_2.jpg"
        ];

    $scope.images=data;
});