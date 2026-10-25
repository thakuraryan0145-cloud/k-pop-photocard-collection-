
export const registerUser = (user) => {
  const savedUser = JSON.parse(
    localStorage.getItem("user") || "null"
  );

  if (savedUser && savedUser.email === user.email) {
    return {
      success: false,
      message: "An account with this email already exists.",
    };
  }

  const safeUser = {
    email: user.email,
    displayName: user.displayName,
  };

  localStorage.setItem("user", JSON.stringify(safeUser));

  return {
    success: true,
    message: "Registration successful!",
  };
};

export const loginUser = (email, _password) => {
  const savedUser = JSON.parse(
    localStorage.getItem("user") || "null"
  );

  if (!savedUser) {
    return {
      success: false,
      message: "No account found. Please register first.",
    };
  }

  if (savedUser.email !== email) {
    return {
      success: false,
      message: "No account found for this email.",
    };
  }

  return {
    success: true,
    message: "Login successful!",
  };
};
