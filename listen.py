def server_loop():
  global target
  # if no target is defined, we listen on all interfaces
  if not len(target):
    target = "0.0.0.0"
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.bind((target,port))
  16   Chapter 2server.listen(5)
  
  while True:
    client_socket, addr = server.accept()
    # spin off a thread to handle our new client
    client_thread = threading.Thread(target=client_handler, ¬
    args=(client_socket,))
    client_thread.start()
    
  def run_command(command):
  # trim the newline
    command = command.rstrip()
    u
    # run the command and get the output back
  try:
    output = subprocess.check_output(command,stderr=subprocess. ¬
    STDOUT, shell=True)
  except:
    output = "Failed to execute command.\r\n"
    # send the output back to the client
  return output
