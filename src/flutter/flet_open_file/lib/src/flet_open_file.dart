import 'package:flet/flet.dart';
import 'package:flutter/material.dart';
import 'package:open_file/open_file.dart';

class FletOpenFileControl extends StatelessWidget {
  final Control? parent;
  final Control control;

  const FletOpenFileControl({
    super.key,
    required this.parent,
    required this.control,
  });

  @override
  Widget build(BuildContext context) {
    Future<void> openFile(String filePath) async {
      await OpenFile.open(filePath);
    }

    final String filePath = control.attrString("value", "")!;
    final String infoText = control.attrString("text", "")!;

    return layoutControl(
      context,
      ElevatedButton(
        onPressed: () => openFile(filePath),
        child: Text(
          infoText,
          style: TextStyle(color: Colors.white),
        ),
      ),
      parent,
      control,
    );
  }
}


