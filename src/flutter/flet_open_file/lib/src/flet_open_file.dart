import 'package:flet/flet.dart';
import 'package:flutter/material.dart';
import 'package:open_file/open_file.dart';

import 'dart:async';
import 'dart:convert';

import 'package:flutter/foundation.dart';


class OpenFileService extends FletService {
  OpenFileService({required super.control});

  String? _path;

  @override
  void init() {
    super.init();
    debugPrint("OpenFile(${control.id}).init: ${control.properties}");
    control.addInvokeMethodListener(_invokeMethod);
    update();
  }

  @override
  void update() {
    debugPrint("OpenFile(${control.id}).update: ${control.properties}");

    var path = control.getString("path", "")!;

    () async {
      bool pathChanged = false;
      if (path != "" && path != _path) {
        _path = path;
        pathChanged = true;
      }

      if (pathChanged) {
        control.triggerEvent("loaded");
      }
    }();
  }

  Future<dynamic> _invokeMethod(String name, dynamic args) async {
    debugPrint("OpenFile.$name($args)");
    switch (name) {
      case "open":
        await openFile(args["path"])
      default:
        throw Exception("Unknown OpenFile method: $name");
    }
  }
}


