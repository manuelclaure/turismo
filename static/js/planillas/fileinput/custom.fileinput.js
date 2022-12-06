$('#fichero').fileinput({
    language: 'es',
    previewFileIcon: '<i class="fa fa-file"></i>',
    allowedPreviewTypes: null, // set to empty, null or false to disable preview for all types
    showUpload: false,
    maxFileCount: 1,
    allowedFileExtensions: ['xls', 'xlsx'],
    previewFileIconSettings: {'xlsx': '<i class="fa fa-file-excel-o text-success"></i>', 'xls': '<i class="fa fa-file-excel-o text-success"></i>'},
});