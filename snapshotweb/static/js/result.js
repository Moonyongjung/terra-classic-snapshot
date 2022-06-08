$('#snapshot_info_submit').click(function(){
    var blockHeight = $('#blockHeight').val()
    var contractAddress = $('#contractAddress').val()
    var accountAddress = $('#accountAddress').val()

    $(document).ready(function(){
        $.ajax({
            url: 'snapshotinfo/',
            type: 'POST',
            data: {
                'blockHeight': blockHeight,
                'contractAddress' : contractAddress,
                'accountAddress' : accountAddress
            },
            data_type: 'json',
            success: function(data){
                console.log("success")
            },
            error:function(data){
                alert("code:"+request.status+"\n"+"message:"+request.responseText+"\n"+"error:"+error);
            }
        });
    });
})