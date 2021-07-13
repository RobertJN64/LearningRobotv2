//custom blocks
//normal
Blockly.Python['move_fd'] = function (block) {
  var code = "robot.moveFD(10)\n";
  return code
};


Blockly.Python['turn'] = function(block) {
  var dropdown_direction = block.getFieldValue('direction');
  if(dropdown_direction == "left") {
    return 'robot.left(90)\n'
  }

  else {
    return 'robot.right(90)\n'
  }
};

//basic
Blockly.Python['basic_fd'] = function (block) {
  var code = "robot.moveFD(10)\n";
  return code
};

Blockly.Python['basic_left'] = function (block) {
  var code = "robot.left(90)\n";
  return code
};


Blockly.Python['basic_right'] = function (block) {
  var code = "robot.right(90)\n";
  return code
};

//params
Blockly.Python['advanced_move_fd'] = function(block) {
  var value_distance = Blockly.Python.valueToCode(block, 'distance', Blockly.Python.ORDER_ATOMIC);
  var code = 'robot.moveFD(' + value_distance + ')\n';
  return code;
};

Blockly.Python['advanced_turn'] = function(block) {
  var dropdown_direction = block.getFieldValue('direction');
  var degrees = Blockly.Python.valueToCode(block, 'degrees', Blockly.Python.ORDER_ATOMIC);
  if(dropdown_direction == "left") {
    return 'robot.left(' + degrees + ')\n'
  }

  else {
    return 'robot.right(' + degrees + ')\n'
  }
};

Blockly.Python['basic_loop'] = function(block) {
  var value_basic_counter = Blockly.Python.valueToCode(block, 'basic_counter', Blockly.Python.ORDER_ATOMIC);
  var statements_loop_code = Blockly.Python.statementToCode(block, 'loop_code');
  statements_loop_code = Blockly.Python.addLoopTrap(statements_loop_code, block) || Blockly.Python.PASS;
  var loopVar = Blockly.Python.nameDB_.getDistinctName(
      'count_basic', Blockly.VARIABLE_CATEGORY_NAME);
  var code = 'for ' + loopVar + ' in range(' + value_basic_counter + '):\n' + statements_loop_code;
  return code;
};

Blockly.Python['python_executor'] = function(block) {
  var text_code = block.getFieldValue('code');
  return text_code + '\n';
};

Blockly.Python['basic_timer'] = function(block) {
  var code = 'robot.wait(5)\n';
  return code;
};

Blockly.Python['timer'] = function(block) {
  var seconds = Blockly.Python.valueToCode(block, 'seconds', Blockly.Python.ORDER_ATOMIC);
  var code = 'robot.wait(' + seconds + ')\n';
  return code;
};

Blockly.Python['motor_controller'] = function(block) {
  var lm = Blockly.Python.valueToCode(block, 'left_motor', Blockly.Python.ORDER_ATOMIC);
  var rm = Blockly.Python.valueToCode(block, 'right_motor', Blockly.Python.ORDER_ATOMIC);
  var code = 'robot.runMotors(' + lm + ", " + rm + ")\n";
  return code;
};

Blockly.Python['stop_motors'] = function(block) {
  var code = 'robot.runMotors(0,0)\n';
  return code;
};
