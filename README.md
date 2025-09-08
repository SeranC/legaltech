# Legal Tech Assistant

A comprehensive web application designed to streamline legal workflows for beverage distribution agreements. This Flask-based application provides AI-powered tools for agreement replication, contract analysis, financial assessment, and knowledge management.

## 🚀 Features

### Core Workflows

#### 1. **Agreement Replication**
- Upload existing agreements and replicate them for different states
- AI-powered analysis of state-specific legal requirements
- Automated modification suggestions for compliance
- Batch processing for multiple target states
- Download replicated agreements with state-specific modifications

#### 2. **Create New Agreement**
- Multi-step wizard interface for creating new distribution agreements
- AI-powered recommendations for standard clauses
- Product category-specific templates
- State-specific legal compliance checks
- Real-time validation and suggestions

#### 3. **Contract Q&A**
- Interactive chat interface for contract analysis
- AI-powered question answering with source citations
- Contract selection and analysis
- Real-time usage statistics and analytics
- Hover tooltips with section snippets
- Clickable source references for document downloads

#### 4. **Financial Analysis**
- Comprehensive financial obligation extraction
- Payment term analysis and visualization
- Risk assessment and alerts
- Contract analysis details with dark mode interface
- Real-time financial metrics and reporting

#### 5. **Term Sheet Generation**
- Automated term sheet creation from agreements
- Template-based generation with customization
- Export capabilities for further review

#### 6. **Knowledge Base**
- Centralized repository of legal documents and templates
- Search and categorization functionality
- Document management and version control
- Dark mode interface for enhanced readability

### User Management

#### Role-Based Access Control
- **Legal Team**: Full access to all workflows and features
- **Finance Team**: Access to financial analysis, contract Q&A, and knowledge base
- **Business Team**: Access to contract Q&A and knowledge base

#### Product Categories
- Wine distribution agreements
- Spirit distribution agreements
- Ready-to-Drink (RTD) beverage agreements
- Non-Alcoholic beverage agreements
- Beer distribution agreements

## 🛠️ Technology Stack

### Backend
- **Flask 2.3.3** - Web framework
- **Python 3.x** - Programming language
- **Jinja2 3.1.2** - Template engine
- **Werkzeug 2.3.7** - WSGI toolkit

### Frontend
- **Bootstrap 5** - UI framework
- **JavaScript (ES6+)** - Client-side scripting
- **CSS3** - Styling with custom dark theme
- **Bootstrap Icons** - Icon library
- **Rich** - Enhanced UI components

### Key Libraries
- **python-dotenv** - Environment variable management
- **uuid** - Unique identifier generation
- **datetime** - Date and time handling
- **json** - Data serialization
- **random** - Mock data generation

## 📁 Project Structure

```
legal-tech-assistant/
├── app.py                          # Main Flask application
├── requirements.txt                # Python dependencies
├── README.md                      # Project documentation
├── mock_data/                     # Sample data for demo
│   ├── agreements/               # Sample agreement files
│   ├── financial_data/           # Financial analysis data
│   ├── templates/                # Document templates
│   └── user_sessions/            # User session data
├── static/                       # Static assets
│   ├── css/
│   │   ├── colors.css           # Color scheme definitions
│   │   └── styles.css           # Main stylesheet
│   ├── js/
│   │   └── main.js              # Client-side JavaScript
│   └── assets/
│       └── images/              # Image assets
└── templates/                    # HTML templates
    ├── base.html                # Base template
    ├── dashboard.html           # Main dashboard
    ├── login.html               # Authentication
    ├── select_category.html     # Product category selection
    ├── agreement_replication.html
    ├── create_agreement.html
    ├── contract_qa.html
    ├── financial_analysis.html
    ├── knowledge_base.html
    ├── term_sheet.html
    └── upload.html
```

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd legal-tech-assistant
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the application**
   Open your browser and navigate to `http://localhost:5000`

### Demo Login
The application includes mock users for demonstration:
- **Legal Team**: `sarah.johnson@bbg.com`
- **Finance Team**: `mike.chen@bbg.com`
- **Business Team**: `jennifer.smith@bbg.com`

## 🎨 UI/UX Features

### Dark Mode Theme
- Consistent dark theme across all pages
- High contrast for improved readability
- Modern glassmorphism effects
- Smooth animations and transitions

### Responsive Design
- Mobile-first approach
- Bootstrap-based responsive grid
- Adaptive layouts for all screen sizes
- Touch-friendly interface elements

### Interactive Elements
- Real-time form validation
- Dynamic content loading
- Smooth page transitions
- Interactive charts and visualizations
- Hover effects and tooltips

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the project root:
```env
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
```

### Product Categories
Modify `PRODUCT_CATEGORIES` in `app.py` to add or update product categories.

### User Roles
Update `USER_ROLES` in `app.py` to modify permissions and access levels.

## 📊 API Endpoints

### Authentication
- `POST /login` - User authentication
- `GET /logout` - User logout
- `GET /select-category` - Product category selection

### Workflows
- `GET /agreement-replication` - Agreement replication interface
- `GET /create-agreement` - Agreement creation interface
- `GET /contract-qa` - Contract Q&A interface
- `GET /financial-analysis` - Financial analysis interface
- `GET /knowledge-base` - Knowledge base interface
- `GET /term-sheet` - Term sheet generation interface

### API Endpoints
- `POST /api/start-session` - Start a new workflow session
- `POST /api/send-message` - Send message to AI assistant
- `POST /api/agreement-replication` - Process agreement replication
- `GET /api/download-replicated-agreement/<state>` - Download replicated agreement

## 🧪 Testing

### Mock Data
The application includes comprehensive mock data for testing:
- Sample agreements for different product categories
- Financial data for analysis workflows
- User sessions and permissions
- Template documents

### Demo Scenarios
1. **Agreement Replication**: Upload a sample agreement and replicate for multiple states
2. **Contract Q&A**: Ask questions about uploaded contracts
3. **Financial Analysis**: Analyze financial obligations and payment terms
4. **Create Agreement**: Use the wizard to create new agreements

## 🔒 Security Features

### Authentication
- Session-based authentication
- Role-based access control
- Secure session management

### Data Protection
- Input validation and sanitization
- CSRF protection
- Secure file upload handling

## 🚀 Deployment

### Production Considerations
1. **Environment Variables**: Set production environment variables
2. **Database**: Configure production database
3. **Static Files**: Serve static files through a web server
4. **SSL**: Enable HTTPS for secure communication
5. **Logging**: Configure application logging

### Docker Deployment
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Support

For support and questions:
- Create an issue in the repository
- Contact the development team
- Check the documentation for common solutions

## 🔄 Version History

### v1.0.0
- Initial release
- Core workflow implementations
- Dark mode theme
- Role-based access control
- Mock data and demo functionality

---

**Legal Tech Assistant** - Streamlining legal workflows for the modern beverage industry.
