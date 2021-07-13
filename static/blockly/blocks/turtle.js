//normal
Blockly.Blocks['move_fd'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Move forward 🠅");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(0);
 this.setTooltip("Moves the robot forward!");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['turn'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Turn");
    this.appendDummyInput()
        .appendField(new Blockly.FieldDropdown([["left ⟲","left"], [" right ⟳","right"]]), "direction");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(0);
 this.setTooltip("Turns the robot!");
 this.setHelpUrl("");
  }
};

//basic
Blockly.Blocks['basic_fd'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldImage("/static/block_icons/fd_arrow.png", 30, 30, { alt: "up arrow", flipRtl: "FALSE" }));
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
 this.setTooltip("");
 this.setHelpUrl("Move forward!");
  }
};

Blockly.Blocks['basic_left'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldImage("/static/block_icons/left_arrow.png", 30, 30, { alt: "left arrow", flipRtl: "FALSE" }));
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
 this.setTooltip("");
 this.setHelpUrl("Turn left!");
  }
};

Blockly.Blocks['basic_right'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldImage("/static/block_icons/right_arrow.png", 30, 30, { alt: "right arrow", flipRtl: "FALSE" }));
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
 this.setTooltip("");
 this.setHelpUrl("Turn right!");
  }
};

//params
Blockly.Blocks['advanced_move_fd'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Move forward 🠅");
    this.appendValueInput("distance")
        .setCheck("Number")
        .appendField("Distance:");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(0);
 this.setTooltip("Moves the robot forward!");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['advanced_turn'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Turn");
    this.appendDummyInput()
        .appendField(new Blockly.FieldDropdown([["left ⟲","left"], [" right ⟳","right"]]), "direction");
    this.appendValueInput("degrees")
        .setCheck(null);
    this.appendDummyInput()
        .appendField("degrees");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(0);
 this.setTooltip("Turns the robot!");
 this.setHelpUrl("");
  }
};


Blockly.Blocks['basic_loop'] = {
  init: function() {
    this.appendValueInput("basic_counter")
        .setCheck("Number")
        .appendField(new Blockly.FieldImage("/static/block_icons/loop_top.png", 50, 30, { alt: "->", flipRtl: "FALSE" }))
        .appendField("Loop | Count:");
    this.appendStatementInput("loop_code")
        .setCheck(null)
        .appendField(new Blockly.FieldImage("/static/block_icons/loop_mid.png", 10, 50, { alt: "|", flipRtl: "FALSE" }));
    this.appendDummyInput()
        .appendField(new Blockly.FieldImage("/static/block_icons/loop_bottom.png", 50, 30, { alt: "<-", flipRtl: "FALSE" }));
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(40);
 this.setTooltip("Easier to read loop!");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['python_executor'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldTextInput("print(\"this is custom python code!\")"), "code");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
 this.setTooltip("Runs custom python code. Don't try to get fancy, we block imports...");
 this.setHelpUrl("");
 }
};

Blockly.Blocks['basic_timer'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldImage("static/block_icons/timer.png", 30, 30, { alt: "*", flipRtl: "FALSE" }));
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
 this.setTooltip("Waits for 5 seconds.");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['timer'] = {
  init: function() {
    this.appendValueInput("seconds")
        .setCheck(null)
        .appendField("Sleep:");
    this.appendDummyInput()
        .appendField("seconds");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(0);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['motor_controller'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Motor Controller");
    this.appendValueInput("left_motor")
        .setCheck("Number")
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField("Left motor:");
    this.appendValueInput("right_motor")
        .setCheck("Number")
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField("Right motor:");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(0);
 this.setTooltip("Set the power of each motor");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['stop_motors'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Stop Motors");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(0);
 this.setTooltip("Stops motors");
 this.setHelpUrl("");
  }
};