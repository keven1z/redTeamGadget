/*
* 根据类型改变输入的框格式，以符合具体漏洞情况
* */

function add_url_shell_html(name) {
    let input_view = `
    <span class="h2">${name}</span>
                <div class="btn-toolbar mb-2 mb-md-0">
                    <div class="btn-group me-2">
                        <span class="input-group-text" id="inputGroup-sizing-default" >URL</span>
                        <input type="text" class="form-control" aria-label="Sizing example input"
                               aria-describedby="inputGroup-sizing-default" id="${name}_url" >
                       
                        <span class="input-group-text" id="inputGroup-sizing-default"  >VPS</span>
                        <input type="text" class="form-control" aria-label="Sizing example input"
                               aria-describedby="inputGroup-sizing-default" id="${name}_vps" >
                    </div>
                    <div class="btn-group me-2">
                        <button type="button" class="btn btn-sm btn-outline-secondary" id="${name}_run" onclick="shell_run('${name}',3)">运行</button>
                    </div>

                </div>
    `;

    let show_html = `
    <div class="row">
                    
                    <div class="col-sm">
                        <h3>命令执行结果</h3>
    　　                  <!-- loading -->
                        <div class="align-items-center" style="display: none" id="${name}_spinner">
                          <strong>运行中...</strong>
                          <div class="spinner-border ml-auto" role="status" aria-hidden="true"></div>
                        </div>
                        <textarea class="form-control" rows="20" id="${name}_show"></textarea>
                    </div>

                </div>
    `
    $("#container_plugin").empty();
    $("#container_plugin").append(show_html);
    $("#div_plugin_input").empty();
    $("#div_plugin_input").append(input_view);
}

function add_CMD_html(name) {
    let input_view = `
    <span class="h2">${name}</span>
                <div class="btn-toolbar mb-2 mb-md-0">
                    <div class="btn-group me-2">
                        <span class="input-group-text" id="inputGroup-sizing-default" >ip</span>
                        <input type="text" class="form-control" aria-label="Sizing example input"
                               aria-describedby="inputGroup-sizing-default" id="${name}_ip" >
                        <span class="input-group-text" id="inputGroup-sizing-default"  >端口</span>
                        <input type="text" class="form-control" aria-label="Sizing example input"
                               aria-describedby="inputGroup-sizing-default" id="${name}_port" >
                        <span class="input-group-text" id="inputGroup-sizing-default"  >命令</span>
                        <input type="text" class="form-control" aria-label="Sizing example input"
                               aria-describedby="inputGroup-sizing-default" id="${name}_cmd" >
                    </div>
                    <div class="btn-group me-2">+
                        <button type="button" class="btn btn-sm btn-outline-secondary" id="${name}_run" onclick="cmd_run('${name}',2)" >运行</button>
                    </div>

                </div>
    `;
    let show_html = `
    <div class="row">
                    
                    <div class="col-sm">
                        <h3>命令执行结果</h3>
    　　                  <!-- loading -->
                        <div class="align-items-center" style="display: none" id="${name}_spinner">
                          <strong>运行中...</strong>
                          <div class="spinner-border ml-auto" role="status" aria-hidden="true"></div>
                        </div>
                        <textarea class="form-control" rows="20" id="${name}_show"></textarea>
                    </div>

                </div>
    `
    $("#container_plugin").empty();
    $("#container_plugin").append(show_html);
    $("#div_plugin_input").empty();
    $("#div_plugin_input").append(input_view);
}

function add_URL_CMD_html(name) {
    let input_view = `
    <span class="h2">${name}</span>
                <div class="btn-toolbar mb-2 mb-md-0">
                    <div class="btn-group me-2">
                        <span class="input-group-text" id="inputGroup-sizing-default" >URL</span>
                        <input type="text" class="form-control" aria-label="Sizing example input"
                               aria-describedby="inputGroup-sizing-default" id="${name}_url" >
                        <span class="input-group-text" id="inputGroup-sizing-default"  >命令</span>
                        <input type="text" class="form-control" aria-label="Sizing example input"
                               aria-describedby="inputGroup-sizing-default" id="${name}_cmd" >
                    </div>
                    <div class="btn-group me-2">
                        <button type="button" class="btn btn-sm btn-outline-secondary" id="${name}_run" onclick="url_cmd_run('${name}',1)" >运行</button>
                    </div>

                </div>
    `;
    let show_html = `
    <div class="row">
                    
                    <div class="col-sm">
                        <h3>命令执行结果</h3>
    　　                  <!-- loading -->
                        <div class="align-items-center" style="display: none" id="${name}_spinner">
                          <strong>运行中...</strong>
                          <div class="spinner-border ml-auto" role="status" aria-hidden="true"></div>
                        </div>
                        <textarea class="form-control" rows="20" id="${name}_show"></textarea>
                    </div>

                </div>
    `
    $("#container_plugin").empty();
    $("#container_plugin").append(show_html);
    $("#div_plugin_input").empty();
    $("#div_plugin_input").append(input_view);
}

function cmd_run(name, type) {
    $("#" + name + "_show").empty()
    $("#" + name + "_spinner").show();
    let cmd = $("#" + name + "_cmd").val();
    cmd = cmd.replaceAll("&","%26")
    $.ajax({
        url: "/run?name=" + name + "&type=" + type + "&ip=" + $("#" + name + "_ip").val() + '&port=' + $("#" + name + "_port").val() + '&cmd=' +  cmd,
        type: 'GET',
        async: true,
        cache: false,
        contentType: false,
        processData: false,
        success: function (data) {
            $("#" + name + "_show").val(JSON.parse(data).data)
            $("#" + name + "_spinner").hide();
        },
        error: function (jqXHR, textStatus, errorThrown) {
            $("#" + name + "_spinner").removeClass("d-flex");
        }
    });
}

function url_cmd_run(name, type) {
    $("#" + name + "_show").empty()
    $("#" + name + "_spinner").show();
    let cmd = $("#" + name + "_cmd").val();
    cmd = cmd.replaceAll("&","%26")
    $.ajax({
        url: "/run?name=" + name + "&type=" + type + "&url=" + $("#" + name + "_url").val() + '&cmd=' + cmd,
        type: 'GET',
        async: true,
        cache: false,
        contentType: false,
        processData: false,
        success: function (data) {
            $("#" + name + "_show").val(JSON.parse(data).data)
            $("#" + name + "_spinner").hide();
        },
        error: function (jqXHR, textStatus, errorThrown) {
            $("#" + name + "_spinner").removeClass("d-flex");
        }
    });
}

function shell_run(name, type) {
    $("#" + name + "_show").empty()
    $("#" + name + "_spinner").show();
    $.ajax({
        url: "/run?name=" + name + "&type=" + type + "&url=" + $("#" + name + "_url").val() + '&vps=' + $("#" + name + "_vps").val(),
        type: 'GET',
        async: true,
        cache: false,
        contentType: false,
        processData: false,
        success: function (data) {
            $("#" + name + "_show").val(JSON.parse(data).data)
            $("#" + name + "_spinner").hide();
        },
        error: function (jqXHR, textStatus, errorThrown) {
            $("#" + name + "_spinner").removeClass("d-flex");
        }
    });
}
