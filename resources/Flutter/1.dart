import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text('Flutter Text and Image Example'),
        ),
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Image.network(
                'https://avatars.githubusercontent.com/u/110104434?v=4',
                height: 100, // Adjust the height as needed
              ),
              SizedBox(height: 20), // Space between image and text
              Text(
                'Hello, Flutter!',
                style: TextStyle(
                  fontSize: 20,
                  color: Colors.blue,
                  fontWeight: FontWeight.bold,
                ),
              ),
              SizedBox(height: 20), // Space between text and container
              Container(
                padding: EdgeInsets.all(10),
                margin: EdgeInsets.all(20),
                decoration: BoxDecoration(
                  color: Colors.blue,
                  borderRadius: BorderRadius.circular(10),
                ),
                child: Text(
                  'This is a container',
                  style: TextStyle(
                    color: Colors.white, // White text for visibility
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
