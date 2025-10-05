import 'package:flet/flet.dart';

import 'flet_open_file.dart';

class Extension extends FletExtension {
  @override
  FletService? createService(Control control) {
    switch (control.type) {
      case "OpenFile":
        return OpenFileService(control: control);
      default:
        return null;
    }
  }
}
